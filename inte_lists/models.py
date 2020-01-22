from edc_list_data.model_mixins import ListModelMixin


class BaselineConditions(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Baseline Conditions"
        verbose_name_plural = "Baseline Conditions"


class OffstudyReasons(ListModelMixin):
    class Meta(ListModelMixin.Meta):
        verbose_name = "Offstudy Reasons"
        verbose_name_plural = "Offstudy Reasons"
