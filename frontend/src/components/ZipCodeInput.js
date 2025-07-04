import "../styles/ZipCodeInput.css"

function ZipCodeInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="zip-code-input">Arrondissement</label>
            <input type="text" 
            id="zip-code-input" 
            name="zip-code-input" 
            onChange={(e) => sendInputDataToForm(e.target.value)}
            required/>
        </div>
        
    )
}

export default ZipCodeInput