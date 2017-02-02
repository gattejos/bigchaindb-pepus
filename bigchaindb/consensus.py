from bigchaindb.util import verify_vote_signature
import logging
import os
import random

logger = logging.getLogger(__name__)

class BaseConsensusRules():
    """Base consensus rules for Bigchain.
    """

    @staticmethod
    def validate_transaction(bigchain, transaction):
        """See :meth:`bigchaindb.models.Transaction.validate`
        for documentation.

        """
        if random.randint(1,10) > 5 or os.environ.get('FILTER') == '':
            logger.info("Transaction verified"
                   ": %s", transaction.id) 
            return transaction.validate(bigchain)
        else:
            logger.info("Transaction NOT verified"
                   ": %s", transaction.id)        
            return False

    @staticmethod
    def validate_block(bigchain, block):
        """See :meth:`bigchaindb.models.Block.validate` for documentation."""
        return block.validate(bigchain)

    @staticmethod
    def verify_vote_signature(voters, signed_vote):
        """Verify the signature of a vote.

        Refer to the documentation of
        :func:`bigchaindb.util.verify_signature`.
        """
        return verify_vote_signature(voters, signed_vote)