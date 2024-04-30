
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start58
solo_miner_base.END_NONCE = nounces.end58
solo_miner_base.LOG_NAME = 'logs/solo_miner58.log'

solo_miner_base.run()
    