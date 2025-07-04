import "../styles/StartButton.css"

function StartButton({onSubmitFormTrigger}) {
    const triggerClickEvent = (e) =>{
        e.preventDefault()
        e.stopPropagation()
        onSubmitFormTrigger()
    }
    return <button type="submit" onClick={triggerClickEvent}>C'est parti !</button>
}

export default StartButton