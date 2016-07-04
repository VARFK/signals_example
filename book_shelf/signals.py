from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from book_shelf.models import *
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=Privileges)
@receiver(pre_delete, sender=Book)
@receiver(pre_delete, sender=User)
@receiver(pre_save, sender=Privileges)
@receiver(pre_save, sender=Book)
@receiver(pre_save, sender=User)
def model_pre_change(sender, **kwargs):
    print '* model_pre_change: {0}'.format(str(sender))
    logger.info('model_pre_change: {0}'.format(str(sender)))


@receiver(post_save, sender=Privileges)
@receiver(post_save, sender=Book)
@receiver(post_save, sender=User)
def model_post_change(sender, **kwargs):
    print '* model_post_change: {0}'.format(str(sender))
    logger.info('model_post_change: {0}'.format(str(sender)))


@receiver(post_delete, sender=Privileges)
@receiver(post_delete, sender=Book)
@receiver(post_delete, sender=User)
def model_post_delete(sender, **kwargs):
    print '* model_post_delete: {0}'.format(str(sender))
    logger.info('model_post_delete: {0}'.format(str(sender)))
