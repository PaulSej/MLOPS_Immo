import "../styles/PseudoInput.css"

function PseudoInput() {
    return (
        <div>
            <label for="pseudo-input">Pseudo</label>
            <input type="text" id="pseudo-input" name="pseudo-input" required/>
        </div>
        
    )
}

export default PseudoInput