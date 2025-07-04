import "../styles/LivingSpaceInput.css"

function ApartmentFloorInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="floor-input">Étage</label>
            <input type="text" 
                   id="floor-input" 
                   name="floor-input" 
                   onChange={(e) => sendInputDataToForm(e.target.value)}
                   required/>
        </div>
        
    )
}

export default ApartmentFloorInput