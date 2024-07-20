
# Facial Attendance API

Welcome to the Facial Attendance API! This open-source project is designed to provide advanced facial recognition functionalities. Whether you're building a attendance management system or a security application, this API has got you covered.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [API Functionality](#api-functionality)
    - [Enrolling a Face](#enrolling-a-face)
    - [Searching for a Face](#searching-for-a-face)
    - [Searching for Similar Faces](#searching-for-similar-faces)
    - [Face Verification](#face-verification)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Facial Attendance API is built using Flask, a lightweight web framework for Python. It leverages the power of facial recognition algorithms to provide accurate and efficient face-related functionalities. With this API, you can easily enroll faces, search for faces, find similar faces, and verify faces.

## Getting Started

To get started with the Facial Attendance API, follow these simple steps:

1. Clone the repository to your local machine:
     ```
     git clone https://github.com/your-username/facial-attendance-api.git
     ```

2. Install the required packages by running the following command:
     ```
     pip install -r requirements.txt
     ```

3. Start the Flask app by running the following command in the terminal:
     ```
     flask run
     ```

Congratulations! You have successfully set up the Facial Attendance API on your local machine.

## API Functionality

The Facial Attendance API provides the following powerful functionalities:

### Enrolling a Face

You can use the API to enroll a face into the provided database. During the enrollment process, the API captures various face attributes such as age, gender, race, and emotion. This information can be used for further analysis or identification purposes.

### Searching for a Face

The API allows you to search for a face in the database. If a match is found, it will return the details of the matched face. In case no match is found, the API will provide the top 109 similar faces available. This feature is particularly useful for attendance management systems or security applications.

### Searching for Similar Faces

The Facial Attendance API also provides a functionality to find similar faces in the database. If an accurate match within the threshold is not found, it will return the top 10 most similar faces. This feature can be used for various applications, such as identifying potential duplicates or finding look-alikes.

### Face Verification

Additionally, the API allows you to verify a face by providing a face image and an ID. It will compare the provided face with the enrolled face associated with the given ID to determine if they belong to the same person. This feature is crucial for identity verification and access control systems.

Please note that this project is a work in progress, and additional features may be added in the future.

## Contributing

We welcome contributions to the Facial Attendance API! If you have any ideas, bug fixes, or improvements, please feel free to submit a pull request. Together, we can make this project even better.

## License

This project is licensed under the MIT License. For more details, please refer to the [LICENSE](LICENSE) file.


This is an open-source project that I created for fun. The Facial Attendance API is built using Flask and provides various functionalities related to facial recognition.

## Getting Started

To run the Flask app, follow these steps:

1. Install the required packages by running the following command:
    ```
    pip install -r requirements.txt
    ```

2. Once the packages are installed, you can start the Flask app by running the following command in the terminal:
    ```
    flask run
    ```

## API Functionality

The Facial Attendance API currently supports the following functionalities:

- Enrolling a Face: You can use the API to enroll a face into the provided database. This process also captures face attributes such as age, gender, race, and emotion.

- Searching for a Face: You can search for a face in the database using the API. If a match is found, it will return the details of the matched face. If no match is found, it will return the top 109 similar faces available.

- Searching for Similar Faces: The Facial Attendance API also provides a functionality to find similar faces in the database. If an accurate match within the threshold is not found, it will return the top 10 most similar faces.

- Face Verification: Additionally, the API allows you to verify a face by providing a face image and an ID. It will compare the provided face with the enrolled face associated with the given ID to determine if they belong to the same person.

Please note that this project is a work in progress, and additional features may be added in the future.

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request. Any contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
