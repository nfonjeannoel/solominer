
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start25
solo_miner_base.END_NONCE = nounces.end25
solo_miner_base.LOG_NAME = 'logs/solo_miner25.log'

solo_miner_base.run()
    