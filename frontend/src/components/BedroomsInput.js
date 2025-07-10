import "../styles/BedroomsInput.css"

function BedroomsInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="bedrooms-input">Nombre de chambres</label>
            <input type="number"
            placeholder="0"
            min="0"
            max="10"
            id="bedrooms-input" 
            name="bedrooms-input" 
            onChange={(e) => sendInputDataToForm(e.target.value)}
            required/>
        </div>
        
    )
}

export default BedroomsInput