# 🧪 Data Processor (Demo)

This is a simplified demo web application that simulates a file-processing backend service. Users can upload any .csv file and select a processing type. The system will always return a dummy result file, regardless of the uploaded content.

## 🛠️ How It Works

1. User uploads a `.csv` file
2. User selects a processing code
3. The backend **ignores the uploaded file**, and instead generates a dummy DataFrame based on the selected code
4. The dummy data is returned as a downloadable `.csv`

> 🔒 Note: Due to the use of internal methods and structures in the real system, this demo version was created to simulate the processing flow without exposing confidential business logic or data. The data returned is mocked and intended solely for demonstration purposes.