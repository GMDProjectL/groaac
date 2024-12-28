import subprocess
import os


def get_audio_track_count(input_file):

    """Get the number of audio tracks in the input file."""

    command = [

        'ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type',

        '-of', 'csv=p=0', input_file

    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    audio_tracks = [line for line in result.stdout.splitlines() if line == 'audio']

    return len(audio_tracks)


def extract_audio_track(input_file, track_number, output_file):

    """Extract a specific audio track and convert it to MP3."""

    command = [

        'ffmpeg', '-y', '-i', input_file, '-map', f'0:a:{track_number}', '-c:a', 'mp3', output_file

    ]

    subprocess.run(command)


def extract_tracks_from_video(input_file, output_directory):
    input_file_name: str = os.path.basename(input_file)
    input_file_name = input_file_name.split('.')[0]
    
    audio_track_count = get_audio_track_count(input_file)
    print(f"Number of audio tracks: {audio_track_count}")

    for track_number in range(audio_track_count):

        output_file = f"{output_directory}/{input_file_name}_{track_number}.mp3"
        print(f"Extracting track {track_number} to {output_file}...")

        extract_audio_track(input_file, track_number, output_file)
        print(f"Track {track_number} extracted successfully.")