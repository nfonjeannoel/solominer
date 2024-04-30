
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start74
solo_miner_base.END_NONCE = nounces.end74
solo_miner_base.LOG_NAME = 'logs/solo_miner74.log'

solo_miner_base.run()
    