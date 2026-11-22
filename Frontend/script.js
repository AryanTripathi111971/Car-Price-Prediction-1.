// ========================================
// FASTAPI BACKEND URL
// ========================================

const API_URL = "http://127.0.0.1:8000/predict";


// ========================================
// GET HTML ELEMENTS
// ========================================

const form =
    document.getElementById("predictionForm");

const predictBtn =
    document.getElementById("predictBtn");

const buttonText =
    document.getElementById("buttonText");

const spinner =
    document.getElementById("spinner");

const result =
    document.getElementById("result");

const price =
    document.getElementById("price");

const errorBox =
    document.getElementById("errorBox");


// ========================================
// FORM SUBMIT
// ========================================

form.addEventListener(
    "submit",
    async function (event) {

        // Stop normal form submission
        event.preventDefault();


        // Hide previous messages
        hideError();

        result.classList.add("hidden");


        // ========================================
        // COLLECT USER INPUT
        // ========================================

        const data = {

            company:
                document
                    .getElementById("company")
                    .value
                    .trim(),

            model:
                document
                    .getElementById("model")
                    .value
                    .trim(),

            year:
                Number(
                    document
                        .getElementById("year")
                        .value
                ),

            km_driven:
                Number(
                    document
                        .getElementById("km_driven")
                        .value
                ),

            fuel:
                document
                    .getElementById("fuel")
                    .value,

            seller_type:
                document
                    .getElementById("seller_type")
                    .value,

            transmission:
                document
                    .getElementById("transmission")
                    .value,

            owner:
                document
                    .getElementById("owner")
                    .value
        };


        // ========================================
        // VALIDATE INPUT
        // ========================================

        if (!validateData(data)) {

            return;
        }


        // Show loading
        setLoading(true);


        try {

            // ========================================
            // SEND DATA TO FASTAPI
            // ========================================

            const response =
                await fetch(
                    API_URL,
                    {

                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(data)
                    }
                );


            // ========================================
            // READ RESPONSE
            // ========================================

            let responseData = {};


            try {

                responseData =
                    await response.json();

            } catch {

                throw new Error(
                    "Invalid response received from server."
                );

            }


            // ========================================
            // HANDLE API ERROR
            // ========================================

            if (!response.ok) {

                let detail =
                    responseData.detail;


                // FastAPI validation errors
                if (Array.isArray(detail)) {

                    detail =
                        detail
                            .map(
                                item => item.msg
                            )
                            .join(", ");
                }


                throw new Error(
                    detail ||
                    "Prediction request failed."
                );
            }


            // ========================================
            // CHECK PRICE
            // ========================================

            if (
                responseData.predicted_price ===
                undefined ||

                responseData.predicted_price ===
                null
            ) {

                throw new Error(
                    "The API did not return a predicted price."
                );
            }


            // ========================================
            // GET PREDICTED PRICE
            // ========================================

            const predictedPrice =
                Number(
                    responseData.predicted_price
                );


            if (
                !Number.isFinite(
                    predictedPrice
                )
            ) {

                throw new Error(
                    "Invalid price returned by the model."
                );
            }


            // ========================================
            // DISPLAY PRICE
            // ========================================

            price.textContent =
                "₹ " +
                Math
                    .round(predictedPrice)
                    .toLocaleString("en-IN");


            // Show result
            result.classList.remove(
                "hidden"
            );


        } catch (error) {

            console.error(
                "Prediction error:",
                error
            );


            // ========================================
            // CONNECTION ERROR
            // ========================================

            if (
                error.name ===
                "TypeError"
            ) {

                showError(
                    "Cannot connect to FastAPI server. " +
                    "Make sure your backend is running at " +
                    "http://127.0.0.1:8000"
                );

            } else {

                showError(
                    error.message
                );
            }


        } finally {

            // Stop loading
            setLoading(false);
        }

    }
);


// ========================================
// VALIDATE FORM DATA
// ========================================

function validateData(data) {


    if (
        !data.company ||
        !data.model
    ) {

        showError(
            "Please enter company and car model."
        );

        return false;
    }


    if (
        !Number.isInteger(data.year) ||
        data.year < 1990 ||
        data.year > 2026
    ) {

        showError(
            "Manufacturing year must be between 1990 and 2026."
        );

        return false;
    }


    if (
        !Number.isInteger(data.km_driven) ||
        data.km_driven < 0
    ) {

        showError(
            "Kilometers driven must be 0 or greater."
        );

        return false;
    }


    if (
        !data.fuel ||
        !data.seller_type ||
        !data.transmission ||
        !data.owner
    ) {

        showError(
            "Please complete all fields."
        );

        return false;
    }


    return true;
}


// ========================================
// LOADING STATE
// ========================================

function setLoading(isLoading) {


    predictBtn.disabled =
        isLoading;


    if (isLoading) {

        buttonText.textContent =
            "Predicting...";

        spinner.classList.remove(
            "hidden"
        );

    } else {

        buttonText.textContent =
            "Predict Price";

        spinner.classList.add(
            "hidden"
        );
    }
}


// ========================================
// SHOW ERROR
// ========================================

function showError(message) {

    errorBox.textContent =
        message;

    errorBox.classList.remove(
        "hidden"
    );
}


// ========================================
// HIDE ERROR
// ========================================

function hideError() {

    errorBox.textContent = "";

    errorBox.classList.add(
        "hidden"
    );
}
