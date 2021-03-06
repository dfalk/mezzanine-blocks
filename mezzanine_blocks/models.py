from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from mezzanine.core.models import Slugged, RichText

class BaseBlock(Slugged):
    login_required = models.BooleanField(_("Login required"), help_text=_("If checked, only logged in users can view this page"), default=False)
    show_title     = models.BooleanField(_("Show title"), help_text=_("If checked, show block title"), default=False)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(BaseBlock, self).save(*args, **kwargs)
        cache.delete('%s%s' % ('mezzanine_blocks', self.slug, ))

    class Meta:
        abstract = True

class Block(BaseBlock):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Block')
        verbose_name_plural = _('Blocks')

class RichBlock(BaseBlock, RichText):
    class Meta:
        verbose_name = _('Rich Block')
        verbose_name_plural = _('Rich Blocks')
