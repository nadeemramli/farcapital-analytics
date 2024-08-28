from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AwarenessMetrics(TimeStampedModel):
    date = models.DateField()
    platform = models.CharField(max_length=50)
    impressions = models.IntegerField()
    reach = models.IntegerField()
    engagement = models.IntegerField()
    clicks = models.IntegerField()
    video_views = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Awareness Metrics"

class AcquisitionMetrics(TimeStampedModel):
    date = models.DateField()
    source = models.CharField(max_length=50)
    registrations = models.IntegerField()
    form_submissions = models.IntegerField()
    landing_page_views = models.IntegerField()
    bounce_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "Acquisition Metrics"

class ActivationMetrics(TimeStampedModel):
    date = models.DateField()
    event_type = models.CharField(max_length=50)
    participants = models.IntegerField()
    engagement_rate = models.FloatField()
    completion_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "Activation Metrics"

class RetentionMetrics(TimeStampedModel):
    date = models.DateField()
    channel = models.CharField(max_length=50)
    active_users = models.IntegerField()
    engagement_rate = models.FloatField()
    churn_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "Retention Metrics"

class ReferralMetrics(TimeStampedModel):
    date = models.DateField()
    referral_source = models.CharField(max_length=100)
    referrals = models.IntegerField()
    conversion_rate = models.FloatField()

    class Meta:
        verbose_name_plural = "Referral Metrics"

class RevenueMetrics(TimeStampedModel):
    date = models.DateField()
    product_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.CharField(max_length=50)
    transactions = models.IntegerField()

    class Meta:
        verbose_name_plural = "Revenue Metrics"

class MarketingActivity(TimeStampedModel):
    date = models.DateField()
    channel = models.CharField(max_length=50)
    campaign_name = models.CharField(max_length=100)
    spend = models.DecimalField(max_digits=10, decimal_places=2)
    target_audience = models.CharField(max_length=100)
    content_type = models.CharField(max_length=50)

class CampaignPerformance(TimeStampedModel):
    campaign_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_spend = models.DecimalField(max_digits=10, decimal_places=2)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2)
    roi = models.FloatField()
    awareness_impact = models.IntegerField()  # e.g., total impressions
    acquisition_impact = models.IntegerField()  # e.g., total registrations
    activation_impact = models.IntegerField()  # e.g., total participants
    retention_impact = models.FloatField()  # e.g., average engagement rate
    referral_impact = models.IntegerField()  # e.g., total referrals

class CustomerJourney(TimeStampedModel):
    customer_id = models.CharField(max_length=100, unique=True)
    first_touch_point = models.CharField(max_length=50)
    last_touch_point = models.CharField(max_length=50)
    total_touchpoints = models.IntegerField()
    days_to_conversion = models.IntegerField(null=True, blank=True)
    lifetime_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
