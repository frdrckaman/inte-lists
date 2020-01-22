from django.conf import settings
from edc_constants.constants import OTHER, UNKNOWN, DEAD, NONE
from edc_list_data import PreloadData
from inte_prn.constants import (
    WITHDRAWAL,
    TRANSFERRED,
    LATE_EXCLUSION,
    OTHER_RX_DISCONTINUATION,
)


list_data = {
    "meta_lists.baselineconditions": [
        ("hypertension", "Hypertension "),
        ("diabetes", "Diabetes"),
        ("hiv_infection", "HIV Infection"),
    ],
    "meta_lists.offstudyreasons": [
        ("completed_followup", "Patient completed 12 months of follow-up"),
        ("clinical_endpoint", "Patient reached a clinical endpoint"),
        ("toxicity", "Patient experienced an unacceptable toxicity"),
        (
            "intercurrent_illness",
            "Intercurrent illness which prevents further treatment",
        ),
        ("lost_to_followup", "Patient lost to follow-up"),
        (DEAD, "Patient reported/known to have died"),
        (WITHDRAWAL, "Patient withdrew consent to participate further"),
        (LATE_EXCLUSION, "Patient fulfilled late exclusion criteria*"),
        (TRANSFERRED, "Patient has been transferred to another health centre"),
        (
            OTHER_RX_DISCONTINUATION,
            "Other condition that justifies the discontinuation of "
            "treatment in the clinician’s opinion (specify below)",
        ),
        (OTHER, ("Other reason (specify below)"),),
    ],
}


if settings.APP_NAME != "inte_lists":
    preload_data = PreloadData(list_data=list_data)
