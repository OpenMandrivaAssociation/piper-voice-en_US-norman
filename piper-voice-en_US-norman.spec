Name:		piper-voice-en_US-norman
Version:	2023.09.23
Release:	1
Summary:	US English male voice for the Piper TTS system
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/en/en_US/norman/medium
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-en
Provides:	piper-voice-en_US

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/norman/medium/en_US-norman-medium.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/norman/medium/en_US-norman-medium.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*
