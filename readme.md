
# Facial Attendance API

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
