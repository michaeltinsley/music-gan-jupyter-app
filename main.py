import streamlit as st
from utils import options

title = st.sidebar.title(
    body="Music StyleGAN App",
)

st.sidebar.markdown(
    body="A Colab hosted StyleGAN app for creating music videos",
)

# YouTube download

st.sidebar.subheader(
    "Video Selection",
)

video_url = st.sidebar.text_input(
    label="Enter YouTube URL",
)

run = st.sidebar.button(
    label="Run",
)

# Output

st.sidebar.markdown(body="---")
st.sidebar.subheader(
    "Download",
)
download = st.sidebar.button(
    label="Download video",
)


st.title(
    body="Configuration",
)

# GPU Info

st.subheader(
    body="GPU Model",
)

st.text(
    body=gpu.instance_gpu(),
)


# Music GAN options

st.subheader(
    "Style GAN Configuration",
)

st.subheader(
    "Initialization",
)

style_dropdown = st.selectbox(
    label="Select pretrained StyleGAN weights",
    options=options.style_gan_choices,
    index=options.style_gan_choices.index("abstract art"),
)


# Video Parameters

video_parameters_expander = st.beta_expander(
    label="Video Parameters",
)

with video_parameters_expander:
    resolution = st.number_input(
        label="Output resolution. Lower is quicker.",
        min_value=240,
        max_value=2048,
        step=120,
        value=480,
    )

    speed_fpm = st.slider(
        label="Speed FPM",
        min_value=1,
        max_value=120,
        step=5,
        value=12,
    )

    start_time = st.number_input(
        label="The start seconds of the video",
        value=0,
        min_value=0,
        step=1,
    )

    length = st.number_input(
        label="The length of video",
        value=60,
        min_value=1,
        step=1,
    )

    entire_video = st.checkbox(
        label="Render entire video",
        value=False,
    )

# Pulse Parameters

pulse_parameters_expander = st.beta_expander(
    label="Pulse parameters",
)
with pulse_parameters_expander:
    pulse_react = st.slider(
        label="The 'strength' of the pulse",
        min_value=0.0,
        max_value=2.0,
        value=0.5,
    )

    pulse_percussive = st.checkbox(
        label="Make the pulse reacts to the audio's percussive elements",
        value=True,
    )

    pulse_harmonic = st.checkbox(
        label="Make the pulse react to the audio's harmonic elements",
        value=False,
    )


# Motion Parameters

motion_parameters_expander = st.beta_expander(
    label="Motion parameters",
)

with motion_parameters_expander:
    motion_react = st.slider(
        label="The 'strength' of the motion",
        min_value=0.0,
        max_value=2.0,
        value=0.5,
    )

    motion_percussive = st.checkbox(
        label="Make the motion reacts to the audio's percussive elements",
        value=True,
    )

    motion_harmonic = st.checkbox(
        label="Make the motion react to the audio's harmonic elements",
        value=False,
    )


# Class Parameters

class_parameters_expander = st.beta_expander(
    label="Class Parameters",
)
with class_parameters_expander:
    class_pitch_react = st.slider(
        label="The 'strength' of the pitch",
        min_value=0.0,
        max_value=2.0,
        value=0.5,
    )

    class_smooth_seconds = st.number_input(
        label="Number of seconds spent smoothly interpolating between each "
        "class vector. The higher the value, the less 'sudden' the "
        "change of class.",
        min_value=1,
        value=1,
        step=1,
    )

    class_complexity = st.slider(
        label="Controls the 'complexity' of images generated. Lower values "
        "tend to generate more simple and mundane images, while higher "
        "values tend to generate more intricate and bizzare objects.",
        min_value=0.0,
        max_value=1.0,
        value=1.0,
    )

    class_shuffle_seconds = st.number_input(
        label="Number of seconds spent smoothly interpolating between each "
        "class vector. The higher the value, the less 'sudden' the "
        "change of class.",
        min_value=1,
        value=15,
        step=1,
    )

# Effects Parameters

effects_parameters_expander = st.beta_expander(
    label="Effects Parameters",
)

with effects_parameters_expander:
    contrast_strength = st.slider(
        label="Strength of default contrast effect",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
    )

    contrast_percussive = st.checkbox(
        label="If enabled, contrast reacts to the audio's percussive elements.",
        value=True,
    )

    flash_strength = st.slider(
        label="Strength of default flash effect",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
    )
    flash_percussive = st.checkbox(
        label="If enabled, flash reacts to the audio's percussive elements.",
        value=True,
    )
