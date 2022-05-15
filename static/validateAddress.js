// Update lat and long input fields with info received from the API
const updateDOM = (result) => {
    console.log(result)
    document.getElementById("lat-field").value = result.features[0].properties.lat
    document.getElementById("long-field").value = result.features[0].properties.lon
    
}

// Make the API call
const makeAPIcall = (street, city, country) => {
    let requestOptions = {
        method: 'GET',
      };
      
      fetch(`https://api.geoapify.com/v1/geocode/search?text=${street}%2C%20${city}%20%2C%20${country}&apiKey=c390c889754e48ba87eee7ba565d131b`, requestOptions)
        .then(response => response.json())
        .then(result => {
            updateDOM(result)
        })
        .catch(error => console.log('error', error));

}

// Validate address
const validateAddress = () => {
    let street = document.getElementById("street").value.replaceAll(' ', '%20')
    let city = document.getElementById("city").value.replaceAll(' ', '%20')
    let country = document.getElementById("country").value.replaceAll(' ', '%20')

    makeAPIcall(street, city, country)
}

// Add event listener to button
const validateBtn = document.getElementById("validate-btn")
validateBtn.addEventListener("click", validateAddress);

