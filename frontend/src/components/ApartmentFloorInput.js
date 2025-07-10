import "../styles/LivingSpaceInput.css"

function ApartmentFloorInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="floor-input">Étage</label>
            <input type="number" 
                    placeholder="0 (RDC)"
                    min="0"
                    max="20" 
                    id="floor-input" 
                    name="floor-input" 
                    onChange={(e) => sendInputDataToForm(e.target.value)}
                    required/>
        </div>
        
    )
}

export default ApartmentFloorInput