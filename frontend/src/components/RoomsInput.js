import "../styles/RoomsInput.css"

function RoomsInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="rooms-input">Nombre de pièces</label>
            <input type="text" 
            id="rooms-input" 
            name="rooms-input" 
            onChange={(e) => sendInputDataToForm(e.target.value)}
            required/>
        </div>
        
    )
}

export default RoomsInput