
import solo_miner_base
import nounces

solo_miner_base.START_NONCE = nounces.start20
solo_miner_base.END_NONCE = nounces.end20
solo_miner_base.LOG_NAME = 'logs/solo_miner20.log'

solo_miner_base.run()
    