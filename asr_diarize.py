import os
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer, SetLogLevel
import wave
import json
import shutil


asrmodel = Model("/home/laishram/workspace/asr_vosk/vosk_General_Hindi_ASR_v1.17_2gram_collection_20_10_22")


def stt(bytess):
    fin = wave.open(bytess,'rb')
    rec = KaldiRecognizer(asrmodel, fin.getframerate())
    while True:
        data = fin.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            pass
        else:
            pass
    asr_out = json.loads(rec.FinalResult())
    decoded_text = asr_out['text']
    if decoded_text == " " or decoded_text == "":
        decoded_text = "silence"
    print(decoded_text)
    return decoded_text

def asr_diarize(filepath):
    

    # file name with extension
    file_name = os.path.basename(filepath)

    # file name without extension
    file_name_without_ext=os.path.splitext(file_name)[0]
    directory = os.path.dirname(filepath)
    print(file_name_without_ext, directory)
    tmp_dir="."+file_name_without_ext
    os.mkdir(tmp_dir,mode=0o777)
    read_file=open(directory+"/diarize_"+file_name_without_ext)
    lines=read_file.readlines()
    read_file.close()
    read_wav = AudioSegment.from_wav(filepath)
    return_decoded_text=""
    for index, eachline in enumerate(lines):
        print(eachline.strip(),"-----------")
        info=eachline.strip().split("\t")
        print(info[0],info[1],info[2])
        start_time=float(info[0])*1000
        end_time=float(info[1])*1000
        speech = read_wav[start_time:end_time]
        new_chunk=tmp_dir+"/"+str(index)+'.wav'
        speech.export(new_chunk, format="wav")
        decoded_text=stt(new_chunk)
        if(info[2]=="1"):
            decoded_text="speaker1: "+decoded_text+"; "
        if(info[2]=="2"):
            decoded_text="speaker2: "+decoded_text+"; "    
        return_decoded_text=return_decoded_text+decoded_text

    shutil.rmtree(tmp_dir, ignore_errors=False, onerror=None)
    return return_decoded_text

print(asr_diarize("/home/laishram/Downloads/8282829536.wav"))