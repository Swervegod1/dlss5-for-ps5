#!/usr/bin/env python3
"""Optional Linux EGL/GLES 3 shader test. No browser, PS5, or Python packages.

Requires system libEGL and a surfaceless GLES 3 driver (Mesa can use software
rendering). This checks shader math, not browser capture or performance.
"""
import ctypes as C
import ctypes.util
from pathlib import Path
import re


def main():
    egl_name = ctypes.util.find_library("EGL")
    if not egl_name:
        raise SystemExit("SKIP: system EGL library unavailable")
    egl = C.CDLL(egl_name)

    def api(name, restype, *args):
        fn = getattr(egl, name)
        fn.restype, fn.argtypes = restype, args
        return fn

    get_proc = api("eglGetProcAddress", C.c_void_p, C.c_char_p)

    def proc(name, restype, *args):
        pointer = get_proc(name.encode())
        if not pointer:
            raise RuntimeError(f"Graphics function unavailable: {name}")
        return C.CFUNCTYPE(restype, *args)(pointer)

    get_display = proc("eglGetPlatformDisplayEXT", C.c_void_p, C.c_uint, C.c_void_p, C.POINTER(C.c_int))
    display = get_display(0x31DD, None, None)
    major, minor = C.c_int(), C.c_int()
    if not api("eglInitialize", C.c_uint, C.c_void_p, C.POINTER(C.c_int), C.POINTER(C.c_int))(display, C.byref(major), C.byref(minor)):
        raise SystemExit("SKIP: surfaceless EGL initialization unavailable")
    api("eglBindAPI", C.c_uint, C.c_uint)(0x30A0)
    attributes = (C.c_int * 13)(0x3033, 1, 0x3040, 0x40, 0x3024, 8, 0x3023, 8, 0x3022, 8, 0x3021, 8, 0x3038)
    config, count = C.c_void_p(), C.c_int()
    api("eglChooseConfig", C.c_uint, C.c_void_p, C.POINTER(C.c_int), C.POINTER(C.c_void_p), C.c_int, C.POINTER(C.c_int))(display, attributes, C.byref(config), 1, C.byref(count))
    if not count.value:
        raise SystemExit("SKIP: GLES 3 configuration unavailable")
    surface = api("eglCreatePbufferSurface", C.c_void_p, C.c_void_p, C.c_void_p, C.POINTER(C.c_int))(display, config, (C.c_int * 5)(0x3057, 32, 0x3056, 32, 0x3038))
    context = api("eglCreateContext", C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p, C.POINTER(C.c_int))(display, config, None, (C.c_int * 3)(0x3098, 3, 0x3038))
    if not context or not surface or not api("eglMakeCurrent", C.c_uint, C.c_void_p, C.c_void_p, C.c_void_p, C.c_void_p)(display, surface, surface, context):
        raise SystemExit("SKIP: GLES context unavailable")
    uint, integer, void, floating = C.c_uint, C.c_int, C.c_void_p, C.c_float
    text = (Path(__file__).resolve().parents[1] / "index.html").read_text()
    shaders = [re.search(r"const " + name + r"=`(.*?)`;", text, re.S).group(1) for name in ["vs", "fs"]]
    create_shader = proc("glCreateShader", uint, uint)
    shader_source = proc("glShaderSource", None, uint, integer, C.POINTER(C.c_char_p), C.POINTER(integer))
    compile_shader = proc("glCompileShader", None, uint)
    get_shader = proc("glGetShaderiv", None, uint, uint, C.POINTER(integer))
    ids = []
    for code, kind in zip(shaders, [0x8B31, 0x8B30]):
        shader = create_shader(kind)
        shader_source(shader, 1, (C.c_char_p * 1)(code.encode()), None)
        compile_shader(shader)
        ok = integer()
        get_shader(shader, 0x8B81, C.byref(ok))
        if not ok.value:
            log = C.create_string_buffer(8192)
            proc("glGetShaderInfoLog", None, uint, integer, C.POINTER(integer), C.c_char_p)(shader, 8192, None, log)
            raise AssertionError(log.value.decode())
        ids.append(shader)
    program = proc("glCreateProgram", uint)()
    for shader in ids:
        proc("glAttachShader", None, uint, uint)(program, shader)
    proc("glLinkProgram", None, uint)(program)
    ok = integer()
    proc("glGetProgramiv", None, uint, uint, C.POINTER(integer))(program, 0x8B82, C.byref(ok))
    assert ok.value, "Program did not link"
    proc("glUseProgram", None, uint)(program)
    vertex_buffer = uint()
    proc("glGenBuffers", None, integer, C.POINTER(uint))(1, C.byref(vertex_buffer))
    proc("glBindBuffer", None, uint, uint)(0x8892, vertex_buffer)
    vertices = (floating * 12)(-1, -1, 1, -1, -1, 1, -1, 1, 1, -1, 1, 1)
    proc("glBufferData", None, uint, C.c_ssize_t, void, uint)(0x8892, C.sizeof(vertices), vertices, 0x88E4)
    pos = proc("glGetAttribLocation", integer, uint, C.c_char_p)(program, b"position")
    proc("glEnableVertexAttribArray", None, uint)(pos)
    proc("glVertexAttribPointer", None, uint, integer, uint, C.c_ubyte, integer, void)(pos, 2, 0x1406, 0, 0, None)
    texture = uint()
    proc("glGenTextures", None, integer, C.POINTER(uint))(1, C.byref(texture))
    proc("glBindTexture", None, uint, uint)(0x0DE1, texture)
    for name, value in [(0x2801, 0x2601), (0x2800, 0x2601), (0x2802, 0x812F), (0x2803, 0x812F)]:
        proc("glTexParameteri", None, uint, uint, integer)(0x0DE1, name, value)
    location = proc("glGetUniformLocation", integer, uint, C.c_char_p)

    def uniform(name, value):
        loc = location(program, name.encode())
        if isinstance(value, tuple):
            proc("glUniform2f", None, integer, floating, floating)(loc, *value)
        elif isinstance(value, int):
            proc("glUniform1i", None, integer, integer)(loc, value)
        else:
            proc("glUniform1f", None, integer, floating)(loc, value)

    for name, value in dict(frame=0, sourceSize=(8., 8.), outputSize=(32., 32.), contrast=0., splitAt=.5, viewMode=1, cubic=1).items():
        uniform(name, value)
    proc("glViewport", None, integer, integer, integer, integer)(0, 0, 32, 32)

    def render(data, sharp=1.):
        uniform("sharpness", sharp)
        pixels = (C.c_ubyte * len(data))(*data)
        proc("glTexImage2D", None, uint, integer, integer, integer, integer, integer, uint, uint, void)(0x0DE1, 0, 0x1908, 8, 8, 0, 0x1908, 0x1401, pixels)
        proc("glDrawArrays", None, uint, integer, integer)(4, 0, 6)
        output = (C.c_ubyte * (32 * 32 * 4))()
        proc("glReadPixels", None, integer, integer, integer, integer, uint, uint, void)(0, 0, 32, 32, 0x1908, 0x1401, output)
        return bytes(output)

    solid = render([80, 120, 160, 255] * 64)
    assert all(abs(solid[i] - [80, 120, 160, 255][i % 4]) <= 3 for i in range(len(solid))), "Flat color drift"
    ramp = []
    for y in range(8):
        for x in range(8):
            a = [60, 70, 85, 115, 160, 180, 190, 195][x]
            ramp.extend([a, a, a, 255])
    uniform("cubic", 0)
    before, after = render(ramp, 0.), render(ramp, 1.)
    delta = sum(abs(before[i] - after[i]) for i in range(0, len(before), 4))
    assert delta > 100, f"Sharpening did not affect edges: {delta}"
    assert min(after[0::4]) >= 60 and max(after[0::4]) <= 195, "Sharpening exceeded the source bounds"
    assert proc("glGetError", uint)() == 0, "GL error"
    renderer = proc("glGetString", C.c_char_p, uint)(0x1F01).decode()
    print(f"PASS: GLSL ES 3 shaders compiled and linked ({renderer})")
    print("PASS: flat-color preservation, active sharpening, bounded output, no GL errors")
    print("Scope: standalone shader only. Browser capture, UI, PS5 hardware, and latency not tested.")
    api("eglMakeCurrent", uint, void, void, void, void)(display, None, None, None)
    api("eglDestroyContext", uint, void, void)(display, context)
    api("eglDestroySurface", uint, void, void)(display, surface)
    api("eglTerminate", uint, void)(display)


if __name__ == "__main__":
    main()
