import "../styles/ZipCodeInput.css"

function ZipCodeInput({onFillInput}) {

    const sendInputDataToForm = (input) => {
        onFillInput(input)
    }

    return (
        <div>
            <label for="zip-code-input">Arrondissement</label>
            <select id="zip-code-input" 
            name="zip-code-input" 
            onChange={(e) => sendInputDataToForm(e.target.value)}
            required>
                <option value="75001">75001</option>
                <option value="75002">75002</option>
                <option value="75003">75003</option>
                <option value="75004">75004</option>
                <option value="75005">75005</option>
                <option value="75006">75006</option>
                <option value="75007">75007</option>
                <option value="75008">75008</option>
                <option value="75009">75009</option>
                <option value="75010">75010</option>
                <option value="75011">75011</option>
                <option value="75012">75012</option>
                <option value="75013">75013</option>
                <option value="75014">75014</option>
                <option value="75015">75015</option>
                <option value="75016">75016</option>
                <option value="75116">75116</option>
                <option value="75017">75017</option>
                <option value="75018">75018</option>
                <option value="75019">75019</option>
                <option value="75020">75020</option>   
            </select>

        </div>
        
    )
}

export default ZipCodeInput