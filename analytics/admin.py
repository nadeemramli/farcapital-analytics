from django.contrib import admin
from .models import (
    AcquisitionMetrics,
    ActivationMetrics,
    AwarenessMetrics,
    CampaignPerformance,
    CustomerJourney,
    MarketingActivity,
    ReferralMetrics,
    RetentionMetrics,
    RevenueMetrics
)

admin.site.register(AcquisitionMetrics)
admin.site.register(ActivationMetrics)
admin.site.register(AwarenessMetrics)
admin.site.register(CampaignPerformance)
admin.site.register(CustomerJourney)
admin.site.register(MarketingActivity)
admin.site.register(ReferralMetrics)
admin.site.register(RetentionMetrics)
admin.site.register(RevenueMetrics)
