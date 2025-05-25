import PseudoInput from "./PseudoInput"
import StartButton from "./StartButton"

import '../styles/GameConfig.css'

function GameConfig() {
    return <div className="gameConfig-panel">
                <PseudoInput/>
                <StartButton/>
            </div>
}

export default GameConfig