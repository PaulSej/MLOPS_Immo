import { useState, useEffect } from "react"


import RoomsInput from "./RoomsInput"
import BedroomsInput from "./BedroomsInput"
import LivingSpaceInput from "./LivingSpaceInput"
import ApartmentsFloorInput from "./ApartmentFloorInput"
import ZipCodeInput from "./ZipCodeInput"
import StartButton from "./StartButton"

import '../styles/GameConfig.css'

function GameConfig() {

    const [numberOfRooms, setNumberOfRooms] = useState(0)
    const [numberOfBedrooms, setNumberOfBedrooms] = useState(0)
    const [livingSpace, setLivingSpace] = useState(0.0)
    const [apartmentFloor, setApartmentFloor] = useState(0)
    const [zipCode, setZipCode] = useState(0)

    const [predicted_price, setPredictedPrice] = useState("_____")


    const handleRoomsNumberData = (roomsNumberInputData) => {
        setNumberOfRooms(roomsNumberInputData);
    }

    const handleBedroomsNumberData = (bedroomsNumberInputData) => {
        setNumberOfBedrooms(bedroomsNumberInputData);
    }

    const handleLivingSpaceData = (livingSpaceInputData) => {
        setLivingSpace(livingSpaceInputData);
    }

    const handleApartmentFloorData = (apartmentFloorInputData) => {
        setApartmentFloor(apartmentFloorInputData);
    }

    const handleZipCodeData = (zipCodeInputData) => {
        setZipCode(zipCodeInputData);
    }




    const sendForm = () =>{

        fetch("http://192.168.1.14:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                    "numberOfRooms": numberOfRooms,
                    "numberOfBedrooms": numberOfBedrooms,
                    "livingSpace": livingSpace,
                    "apartmentFloor": apartmentFloor,
                    "zipCode": zipCode
                })
        })
            .then((response) => response.json())
            .then((price) => {
                console.log(price);
                setPredictedPrice(price)
            })
            .catch((err) => {
                console.log(err.predicted_price);
            });
    }

    /*
    useEffect(() => {

    }, []);
    */

    return <form method="post" action="" className="gameConfig-panel">
                <h2>Caractéristiques du bien</h2>
                <RoomsInput onFillInput={handleRoomsNumberData}/>
                <BedroomsInput onFillInput={handleBedroomsNumberData}/>
                <LivingSpaceInput onFillInput={handleLivingSpaceData}/>
                <ApartmentsFloorInput onFillInput={handleApartmentFloorData}/>
                <ZipCodeInput onFillInput={handleZipCodeData}/>
                <StartButton onSubmitFormTrigger={sendForm}/>
                <strong> { predicted_price }   € </strong>
            </form>
}

export default GameConfig