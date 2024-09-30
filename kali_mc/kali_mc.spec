# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['./'],
    binaries=[],
    datas=[('data/*.*', 'data/'), ('data/sim/*.*', 'data/sim/'), ('report/*.*', 'report/'), ('data/sim/C3/B0/*.*', 'data/sim/C3/B0'), ('data/sim/C4/B0/*.*', 'data/sim/C4/B0'), ('data/sim/C5/B0/*.*', 'data/sim/C5/B0'), ('data/sim/C6/B0/*.*', 'data/sim/C6/B0'), ('data/sim/C7/B0/*.*', 'data/sim/C7/B0'), ('data/sim/C8/B0/*.*', 'data/sim/C8/B0'), ('data/sim/C9/B0/*.*', 'data/sim/C9/B0'), ('data/sim/C10/B0/*.*', 'data/sim/C10/B0'), ('data/sim/C12/B0/*.*', 'data/sim/C12/B0'), ('data/sim/C3/B15/*.*', 'data/sim/C3/B15'), ('data/sim/C4/B15/*.*', 'data/sim/C4/B15'), ('data/sim/C5/B15/*.*', 'data/sim/C5/B15'), ('data/sim/C6/B15/*.*', 'data/sim/C6/B15'), ('data/sim/C7/B15/*.*', 'data/sim/C7/B15'), ('data/sim/C8/B15/*.*', 'data/sim/C8/B15'), ('data/sim/C9/B15/*.*', 'data/sim/C9/B15'), ('data/sim/C10/B15/*.*', 'data/sim/C10/B15'), ('data/sim/C12/B15/*.*', 'data/sim/C12/B15'), ('data/sim/C3/B30/*.*', 'data/sim/C3/B30'), ('data/sim/C4/B30/*.*', 'data/sim/C4/B30'), ('data/sim/C5/B30/*.*', 'data/sim/C5/B30'), ('data/sim/C6/B30/*.*', 'data/sim/C6/B30'), ('data/sim/C7/B30/*.*', 'data/sim/C7/B30'), ('data/sim/C8/B30/*.*', 'data/sim/C8/B30'), ('data/sim/C9/B30/*.*', 'data/sim/C9/B30'), ('data/sim/C10/B30/*.*', 'data/sim/C10/B30'), ('data/sim/C12/B30/*.*', 'data/sim/C12/B30'), ('data/sim/C3/B45/*.*', 'data/sim/C3/B45'), ('data/sim/C4/B45/*.*', 'data/sim/C4/B45'), ('data/sim/C5/B45/*.*', 'data/sim/C5/B45'), ('data/sim/C6/B45/*.*', 'data/sim/C6/B45'), ('data/sim/C7/B45/*.*', 'data/sim/C7/B45'), ('data/sim/C8/B45/*.*', 'data/sim/C8/B45'), ('data/sim/C9/B45/*.*', 'data/sim/C9/B45'), ('data/sim/C10/B45/*.*', 'data/sim/C10/B45'), ('data/sim/C12/B45/*.*', 'data/sim/C12/B45'), ('translations/*.*', 'translations')],
    hiddenimports=['pydicom.encoders.gdcm', 'pydicom.encoders.pylibjpeg'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['local_conf', 'importlib-metadata', 'pre-commit', 'pytest', 'sphinx', 'sphinx-rtd-theme', 'sphinxcontrib-bibtex'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
splash = Splash(
    '.\\ui\\res\\splash-kali.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    splash,
    [],
    exclude_binaries=True,
    name='kali_mc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['ui\\res\\kali_ico.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    splash.binaries,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='kali_mc',
)
