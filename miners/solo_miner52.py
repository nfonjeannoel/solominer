
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start52
solo_miner_base.END_NONCE = nounces.end52
solo_miner_base.LOG_NAME = 'logs/solo_miner52.log'

solo_miner_base.run()
    