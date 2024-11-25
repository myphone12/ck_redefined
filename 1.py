import ctypes
import threading
import time
winmm = ctypes.windll.winmm
 
class Scale:
    Rest = 0
    C8 = 108
    B7 = 107
    A7s = 106
    A7 = 105
    G7s = 104
    G7 = 103
    F7s = 102
    F7 = 101
    E7 = 100
    D7s = 99
    D7 = 98
    C7s = 97
    C7 = 96
    B6 = 95
    A6s = 94
    A6 = 93
    G6s = 92
    G6 = 91
    F6s = 90
    F6 = 89
    E6 = 88
    D6s = 87
    D6 = 86
    C6s = 85
    C6 = 84
    B5 = 83
    A5s = 82
    A5 = 81
    G5s = 80
    G5 = 79
    F5s = 78
    F5 = 77
    E5 = 76
    D5s = 75
    D5 = 74
    C5s = 73
    C5 = 72
    B4 = 71
    A4s = 70
    A4 = 69
    G4s = 68
    G4 = 67
    F4s = 66
    F4 = 65
    E4 = 64
    D4s = 63
    D4 = 62
    C4s = 61
    C4 = 60
    B3 = 59
    A3s = 58
    A3 = 57
    G3s = 56
    G3 = 55
    F3s = 54
    F3 = 53
    E3 = 52
    D3s = 51
    D3 = 50
    C3s = 49
    C3 = 48
    B2 = 47
    A2s = 46
    A2 = 45
    G2s = 44
    G2 = 43
    F2s = 42
    F2 = 41
    E2 = 40
    D2s = 39
    D2 = 38
    C2s = 37
    C2 = 36
    B1 = 35
    A1s = 34
    A1 = 33
    G1s = 32
    G1 = 31
    F1s = 30
    F1 = 29
    E1 = 28
    D1s = 27
    D1 = 26
    C1s = 25
    C1 = 24
    B0 = 23
    A0s = 22
    A0 = 21
 
class Voice:
    X1 = Scale.C2
    X2 = Scale.D2
    X3 = Scale.E2
    X4 = Scale.F2
    X5 = Scale.G2
    X6 = Scale.A2
    X7 = Scale.B2
    L1 = Scale.C3
    L2 = Scale.D3
    L3 = Scale.E3
    L4 = Scale.F3
    L5 = Scale.G3
    L6 = Scale.A3
    L7 = Scale.B3
    M1 = Scale.C4
    M2 = Scale.D4
    M3 = Scale.E4
    M4 = Scale.F4
    M5 = Scale.G4
    M6 = Scale.A4
    M7 = Scale.B4
    H1 = Scale.C5
    H2 = Scale.D5
    H3 = Scale.E5
    H4 = Scale.F5
    H5 = Scale.G5
    H6 = Scale.A5
    H7 = Scale.B5
    LOW_SPEED = 500
    MIDDLE_SPEED = 400
    HIGH_SPEED = 300
    _ = 0xFF
 
def playNote(hmo, channel, instrument, note,velocity, duration=0):
    # 设置乐器
    msg = 0xC0 | channel | (instrument << 8)
    winmm.midiOutShortMsg(hmo, msg)
 
    # 发送 Note On 消息
    msg = 0x90 | channel | (note << 8) | (velocity << 16)
    winmm.midiOutShortMsg(hmo, msg)
 
    if duration:
        # 暂停 duration 秒钟
        time.sleep(duration)
 
        # 发送 Note Off 消息
        msg = 0x80 | channel | (note << 8) | (velocity << 16)
        winmm.midiOutShortMsg(hmo, msg)
 
    return channel | (instrument << 8) | (note << 8) | (velocity << 16) + 0x90
 
def go(handle,instrument,velocity):
    wind=[400,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L3,0,Voice.M5,Voice.M3,300,Voice.L2,Voice.L5,2,Voice._,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L2,0,Voice.M5,Voice.M3,Voice.M2,Voice.M3,Voice.M1,Voice.M2,Voice.L7,Voice.M1,300,Voice.L5,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L3,0,Voice.M5,Voice.M3,300,Voice.L2,Voice.L5,2,Voice._,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L2,0,Voice.M5,Voice.M3,Voice.M2,Voice.M3,Voice.M1,Voice.M2,Voice.L7,Voice.M1,300,Voice.L5,
     0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L3,0,Voice.M5,Voice.M3,300,Voice.L2,Voice.L5,2,Voice._,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L2,0,Voice.M5,Voice.M3,Voice.M2,Voice.M3,Voice.M1,Voice.M2,Voice.L7,Voice.M1,300,Voice.L5,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L3,0,Voice.M5,Voice.M3,300,Voice.L2,Voice.L5,2,Voice._,
     0,Voice.M6,Voice.M3,Voice.M2,Voice.L6,Voice.M3,Voice.L6,Voice.M2,Voice.M3,Voice.L6,Voice._,Voice._,Voice._,
     Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,Voice.M3,Voice.M5,0,Voice.M3,700,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,Voice.M2,Voice.M3,Voice.M2,Voice.M1,300,Voice.L5,Voice._,
     Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,Voice.M3,Voice.M5,0,Voice.M3,700,300,Voice.M2,700,0,Voice.M3,300,Voice.M2,0,Voice.M1,700,300,Voice.M2,Voice._,Voice._,Voice._,
     Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,Voice.M3,Voice.M5,0,Voice.M3,700,300,Voice.M2,700,0,Voice.M3,300,Voice.M2,0,Voice.M1,700,300,Voice.L6,Voice._,
     0,Voice.M3,Voice.M2,Voice.M1,Voice.M2,300,Voice.M1,Voice._,0,Voice.M3,Voice.M2,Voice.M1,Voice.M2,300,Voice.M1,700,0,Voice.L5,Voice.M3,Voice.M2,Voice.M1,Voice.M2,300,Voice.M1,Voice._,Voice._,Voice._,
     Voice.M1,Voice.M2,Voice.M3,Voice.M1,Voice.M6,0,Voice.M5,Voice.M6,300,Voice._,700,0,Voice.M1,300,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice._,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice.M3,0,Voice.H1,Voice.H2,Voice.H1,Voice.M7,300,Voice.M6,Voice.M5,Voice.M6,0,Voice.M5,Voice.M6,Voice._,Voice.M5,Voice.M6,Voice.M5,300,Voice.M6,0,Voice.M5,Voice.M2,300,Voice._,0,Voice.M5,700,300,Voice.M3,Voice._,Voice._,Voice._,
     Voice.M1,Voice.M2,Voice.M3,Voice.M1,Voice.M6,0,Voice.M5,Voice.M6,300,Voice._,700,0,Voice.M1,300,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice._,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice.M3,0,Voice.H1,Voice.H2,Voice.H1,Voice.M7,300,Voice.M6,Voice.M5,Voice.M6,0,Voice.H3,Voice.H3,300,Voice._,Voice.M5,Voice.M6,0,Voice.H3,Voice.H3,300,Voice._,0,Voice.M5,700,300,Voice.M6,Voice._,Voice._,Voice._,Voice._,Voice._,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H2,0,Voice.H1,Voice.M6,300,Voice._,0,Voice.H1,Voice.H1,300,Voice.H2,0,Voice.H1,300,Voice.M6,700,0,Voice._,300,Voice.H1,700,Voice.H3,Voice._,0,Voice.H3,Voice.H4,Voice.H3,Voice.H2,Voice.H3,300,Voice.H2,700,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,300,Voice._,Voice.H3,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,700,300,Voice.H3,700,Voice.H2,0,Voice.H1,Voice.M6,700,300,
     Voice.H3,700,Voice.H2,0,Voice.H1,300,Voice.M6,700,Voice.H1,Voice.H1,Voice._,Voice._,Voice._,Voice._,Voice._,
     0,Voice.M6,300,Voice.H3,700,Voice.H2,0,Voice.H1,Voice.M6,700,300,Voice.H3,Voice.H2,700,300,0,Voice.H1,Voice.M6,300,700,Voice.H1,Voice.H1,Voice._,Voice._,
     0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L3,0,Voice.M5,Voice.M3,300,Voice.L2,Voice.L5,2,Voice._,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L2,0,Voice.M5,Voice.M3,Voice.M2,Voice.M3,Voice.M1,Voice.M2,Voice.L7,Voice.M1,300,Voice.L5,0,Voice.L7,Voice.M1,Voice.M2,Voice.M3,300,Voice.L3,0,Voice.M5,Voice.M3,300,Voice.L2,Voice.L5,2,Voice._,
     0,Voice.M6,Voice.M3,Voice.M2,Voice.L6,Voice.M3,Voice.L6,Voice.M2,Voice.M3,Voice.L6,Voice._,Voice._,Voice._,
     Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,Voice.M3,Voice.M5,0,Voice.M3,700,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,Voice.M2,Voice.M3,Voice.M2,Voice.M1,300,Voice.L5,Voice._,
     Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,Voice.M3,Voice.M5,0,Voice.M3,700,300,Voice.M2,700,0,Voice.M3,300,Voice.M2,0,Voice.M1,700,300,Voice.M2,Voice._,Voice._,Voice._,
     Voice.M2,700,0,Voice.M1,300,Voice.M2,700,0,Voice.M1,300,Voice.M2,Voice.M3,Voice.M5,0,Voice.M3,700,300,Voice.M2,700,0,Voice.M3,300,Voice.M2,0,Voice.M1,700,300,Voice.L6,Voice._,
     0,Voice.M3,Voice.M2,Voice.M1,Voice.M2,300,Voice.M1,Voice._,0,Voice.M3,Voice.M2,Voice.M1,Voice.M2,300,Voice.M1,700,0,Voice.L5,Voice.M3,Voice.M2,Voice.M1,Voice.M2,300,Voice.M1,Voice._,Voice._,Voice._,
     Voice.M1,Voice.M2,Voice.M3,Voice.M1,Voice.M6,0,Voice.M5,Voice.M6,300,Voice._,700,0,Voice.M1,300,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice._,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice.M3,0,Voice.H1,Voice.H2,Voice.H1,Voice.M7,300,Voice.M6,Voice.M5,Voice.M6,0,Voice.M5,Voice.M6,Voice._,Voice.M5,Voice.M6,Voice.M5,300,Voice.M6,0,Voice.M5,Voice.M2,300,Voice._,0,Voice.M5,700,300,Voice.M3,Voice._,Voice._,Voice._,
     Voice.M1,Voice.M2,Voice.M3,Voice.M1,Voice.M6,0,Voice.M5,Voice.M6,300,Voice._,700,0,Voice.M1,300,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice._,Voice.M7,0,Voice.M6,Voice.M7,300,Voice._,Voice.M3,0,Voice.H1,Voice.H2,Voice.H1,Voice.M7,300,Voice.M6,Voice.M5,Voice.M6,0,Voice.H3,Voice.H3,300,Voice._,Voice.M5,Voice.M6,0,Voice.H3,Voice.H3,300,Voice._,0,Voice.M5,700,300,Voice.M6,Voice._,Voice._,Voice._,Voice._,Voice._,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H2,0,Voice.H1,Voice.M6,300,Voice._,0,Voice.H1,Voice.H1,300,Voice.H2,0,Voice.H1,300,Voice.M6,700,0,Voice._,300,Voice.H1,700,Voice.H3,Voice._,0,Voice.H3,Voice.H4,Voice.H3,Voice.H2,Voice.H3,300,Voice.H2,700,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,300,Voice._,Voice.H3,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,700,300,Voice.H3,700,Voice.H2,0,Voice.H1,Voice.M6,700,300,
     Voice.H3,700,Voice.H2,0,Voice.H1,300,Voice.M6,700,Voice.H1,Voice.H1,Voice._,Voice._,Voice._,Voice._,Voice._,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H2,0,Voice.H1,Voice.M6,300,Voice._,0,Voice.H1,Voice.H1,300,Voice.H2,0,Voice.H1,300,Voice.M6,700,0,Voice._,300,Voice.H1,700,Voice.H3,Voice._,0,Voice.H3,Voice.H4,Voice.H3,Voice.H2,Voice.H3,300,Voice.H2,700,
     Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,300,Voice._,Voice.H3,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,700,300,Voice.H3,700,Voice.H2,0,Voice.H1,Voice.M6,700,300,
     Voice.H3,700,Voice.H2,0,Voice.H1,300,Voice.M6,700,Voice.H1,Voice.H1,Voice._,Voice._,Voice._,Voice._,Voice._,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H3,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H6,Voice.H5,300,Voice._,0,Voice.H2,Voice.H3,300,Voice.H2,0,Voice.H1,Voice.M6,300,Voice._,0,Voice.H1,Voice.H1,300,Voice.H2,0,Voice.H1,300,Voice.M6,700,0,Voice._,300,Voice.H1,700,Voice.H3,Voice._,0,Voice.H3,Voice.H4,Voice.H3,Voice.H2,Voice.H3,300,Voice.H2,700,
     Voice.H1,Voice.H2,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,300,Voice._,Voice.H3,Voice.H3,0,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,Voice._,Voice.H6,Voice.H5,700,300,Voice.H3,700,Voice.H2,0,Voice.H1,Voice.M6,700,300,
     Voice.H3,700,Voice.H2,0,Voice.H1,300,Voice.M6,700,Voice.H1,Voice.H1,Voice._,Voice._,Voice._,Voice._,Voice._,
     0,Voice.M6,300,Voice.H3,700,Voice.H2,0,Voice.H1,Voice.M6,700,300,Voice.H3,Voice.H2,700,300,0,Voice.H1,Voice.M6,300,700,Voice.H1,Voice.H1,Voice._,Voice._,Voice._,Voice._,Voice._,Voice._,Voice._,-1
    ]
 
 
    sleep = 0.35
 
    for i in wind:
        if i==-1:
            break
        if i == 0:
            sleep = 0.172
            continue
        if i == 700:
            time.sleep(0.172)
            continue
        if i == 300:
            sleep = 0.35
            continue
        if i == Voice._:
            time.sleep(0.25)
            continue
        back=playNote(handle, 0, instrument, i, velocity,sleep)
        print(back,end="\n")
        #time.sleep(sleep)
 
 
# MIDI_MAPPER 常量
MIDI_MAPPER = 0xFFFFFFFF
 
# 创建一个变量来接收 MIDI 输出句柄
hMidiOut = ctypes.c_void_p()
 
# 调用 midiOutOpen 函数
result = winmm.midiOutOpen(ctypes.byref(hMidiOut), MIDI_MAPPER, 0, 0, 0)
if result == 0:
    print("midiOutOpen succeeded")
    #go(hMidiOut,107)
    thread1 = threading.Thread(target=go,args=(hMidiOut,78,90))
    thread2 = threading.Thread(target=go,args=(hMidiOut,0,127))
    thread1.start()
    thread2.start()
else:
    print("midiOutOpen failed")
 
thread1.join()
thread2.join()
# 关闭 MIDI 输出
winmm.midiOutClose(hMidiOut)