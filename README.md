# audiocl

Командная строка для оффлайн-распознавания речи с помощью Vosk.

## Описание

`audiocl` — простой CLI-инструмент для конвертации аудиофайлов в текст (speech-to-text) с использованием модели Vosk.

## Структура репозитория

```
.
└─ main.py        # Основной скрипт CLI
```

## Требования

* Python 3.8 или выше
* Пакет `vosk`
* Пакет `soundfile` (для чтения аудио)

## Установка

1. Клонируйте репозиторий и перейдите в папку проекта:

   ```bash
   git clone https://github.com/HellDiver830/audiocl.git
   cd audiocl
   ```
2. (Опционально) Создайте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```
3. Установите зависимости:

   ```bash
   pip install vosk soundfile
   ```

## Модель Vosk

Модель **vosk-model-small-ru-0.4** для русского распознавания речи можно скачать и распаковать рядом со скриптом:

```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-ru-0.4.zip
unzip vosk-model-small-ru-0.4.zip -d vosk-model-small-ru-0.4
```

## Использование

```bash
python main.py --model vosk-model-small-ru-0.4 --input audio.wav --output transcript.txt
```

* `--model`  — путь к распакованной папке модели Vosk
* `--input`  — путь к аудиофайлу (.wav, .flac и т.д.)
* `--output` — файл для сохранения распознанного текста

## Пример

```bash
python main.py -m vosk-model-small-ru-0.4 -i samples/recording.wav -o result.txt
cat result.txt
```

## Лицензия

MIT License
