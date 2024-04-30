
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start10
solo_miner_base.END_NONCE = nounces.end10
solo_miner_base.LOG_NAME = 'logs/solo_miner10.log'

solo_miner_base.run()
    