# Mr. Invisible - The Magic Cloak Project

## Real-Time Color Cloak (Invisibility Effect) Using OpenCV

This project implements a "cloak of invisibility" effect using OpenCV, masking out a specified color in a video feed from the camera. Users can interactively adjust the HSV (Hue, Saturation, Value) color range to define the color they want to "cloak," creating a magical effect where the selected color area appears invisible.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/real-time-color-cloak.git
    cd real-time-color-cloak
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

   Or manually install the dependencies listed in [Dependencies](#dependencies).

## Usage

1. Run the Python script:
    ```bash
    python color_cloak.py
    ```

2. The webcam feed will open with a separate window of trackbars labeled `bars` to control the color range.
   - Adjust the trackbars to define the HSV range of the color you want to cloak. The color within this range will become invisible in the video feed.

3. Press `q` to exit the program.

## How It Works

This project uses HSV color masking to achieve the invisibility effect:
1. **Color Selection**: The user selects a color range in HSV space using the trackbars.
2. **Mask Creation**: A binary mask isolates the selected color in the frame.
3. **Inversion and Overlay**: The masked color is hidden by blending with the background, creating an "invisible" area in the original frame.

### Trackbars and Color Control

The following trackbars allow you to fine-tune the color you want to cloak:

- `upper_hue`, `lower_hue`: Control the color range in terms of hue (color type).
- `upper_saturation`, `lower_saturation`: Control the range of color saturation.
- `upper_value`, `lower_value`: Control the range of brightness.

## Dependencies

- [OpenCV](https://opencv.org/) for real-time image processing
- [NumPy](https://numpy.org/) for matrix operations

Install via pip:
```bash
pip install opencv-python numpy
```

## Contributing

Contributions are welcome! If you have suggestions or would like to add more functionality, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
