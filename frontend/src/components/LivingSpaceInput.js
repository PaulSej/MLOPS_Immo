import "../styles/LivingSpaceInput.css"

function LivingSpaceInputInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="living-space-input">Surface</label>
            <input type="text" 
            id="living-space-input" 
            name="living-space-input" 
            onChange={(e) => sendInputDataToForm(e.target.value)}
            required/>
            <em>m²</em>
        </div>
        
    )
}

export default LivingSpaceInputInput