# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 environment: pulumi.Input[str],
                 auxiliary_tenant_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_certificate_password: Optional[pulumi.Input[str]] = None,
                 client_certificate_path: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 custom_correlation_request_id: Optional[pulumi.Input[str]] = None,
                 default_location: Optional[pulumi.Input[str]] = None,
                 default_name: Optional[pulumi.Input[str]] = None,
                 default_naming_prefix: Optional[pulumi.Input[str]] = None,
                 default_naming_suffix: Optional[pulumi.Input[str]] = None,
                 default_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 disable_correlation_request_id: Optional[pulumi.Input[bool]] = None,
                 disable_terraform_partner_id: Optional[pulumi.Input[bool]] = None,
                 oidc_request_token: Optional[pulumi.Input[str]] = None,
                 oidc_request_url: Optional[pulumi.Input[str]] = None,
                 oidc_token: Optional[pulumi.Input[str]] = None,
                 oidc_token_file_path: Optional[pulumi.Input[str]] = None,
                 partner_id: Optional[pulumi.Input[str]] = None,
                 skip_provider_registration: Optional[pulumi.Input[bool]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 use_cli: Optional[pulumi.Input[bool]] = None,
                 use_msi: Optional[pulumi.Input[bool]] = None,
                 use_oidc: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] environment: The Cloud Environment which should be used. Possible values are public, usgovernment and china. Defaults to public.
        :param pulumi.Input[str] client_certificate_password: The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client
               Certificate
        :param pulumi.Input[str] client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
               Principal using a Client Certificate.
        :param pulumi.Input[str] client_id: The Client ID which should be used.
        :param pulumi.Input[str] client_secret: The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.
        :param pulumi.Input[str] custom_correlation_request_id: The value of the x-ms-correlation-request-id header (otherwise an auto-generated UUID will be used).
        :param pulumi.Input[bool] disable_correlation_request_id: This will disable the x-ms-correlation-request-id header.
        :param pulumi.Input[bool] disable_terraform_partner_id: This will disable the Terraform Partner ID which is used if a custom `partner_id` isn't specified.
        :param pulumi.Input[str] oidc_request_token: The bearer token for the request to the OIDC provider. For use When authenticating as a Service Principal using OpenID
               Connect.
        :param pulumi.Input[str] oidc_request_url: The URL for the OIDC provider from which to request an ID token. For use When authenticating as a Service Principal
               using OpenID Connect.
        :param pulumi.Input[str] oidc_token: The OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        :param pulumi.Input[str] oidc_token_file_path: The path to a file containing an OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        :param pulumi.Input[str] partner_id: A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
        :param pulumi.Input[bool] skip_provider_registration: Should the Provider skip registering all of the Resource Providers that it supports, if they're not already registered?
        :param pulumi.Input[str] subscription_id: The Subscription ID which should be used.
        :param pulumi.Input[str] tenant_id: The Tenant ID which should be used.
        :param pulumi.Input[bool] use_cli: Allow Azure CLI to be used for Authentication.
        :param pulumi.Input[bool] use_msi: Allow Managed Service Identity to be used for Authentication.
        :param pulumi.Input[bool] use_oidc: Allow OpenID Connect to be used for authentication
        """
        pulumi.set(__self__, "environment", environment)
        if auxiliary_tenant_ids is not None:
            pulumi.set(__self__, "auxiliary_tenant_ids", auxiliary_tenant_ids)
        if client_certificate_password is not None:
            pulumi.set(__self__, "client_certificate_password", client_certificate_password)
        if client_certificate_path is not None:
            pulumi.set(__self__, "client_certificate_path", client_certificate_path)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if custom_correlation_request_id is not None:
            pulumi.set(__self__, "custom_correlation_request_id", custom_correlation_request_id)
        if default_location is not None:
            pulumi.set(__self__, "default_location", default_location)
        if default_name is not None:
            pulumi.set(__self__, "default_name", default_name)
        if default_naming_prefix is not None:
            pulumi.set(__self__, "default_naming_prefix", default_naming_prefix)
        if default_naming_suffix is not None:
            pulumi.set(__self__, "default_naming_suffix", default_naming_suffix)
        if default_tags is not None:
            pulumi.set(__self__, "default_tags", default_tags)
        if disable_correlation_request_id is not None:
            pulumi.set(__self__, "disable_correlation_request_id", disable_correlation_request_id)
        if disable_terraform_partner_id is not None:
            pulumi.set(__self__, "disable_terraform_partner_id", disable_terraform_partner_id)
        if oidc_request_token is not None:
            pulumi.set(__self__, "oidc_request_token", oidc_request_token)
        if oidc_request_url is not None:
            pulumi.set(__self__, "oidc_request_url", oidc_request_url)
        if oidc_token is not None:
            pulumi.set(__self__, "oidc_token", oidc_token)
        if oidc_token_file_path is not None:
            pulumi.set(__self__, "oidc_token_file_path", oidc_token_file_path)
        if partner_id is not None:
            pulumi.set(__self__, "partner_id", partner_id)
        if skip_provider_registration is not None:
            pulumi.set(__self__, "skip_provider_registration", skip_provider_registration)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if use_cli is not None:
            pulumi.set(__self__, "use_cli", use_cli)
        if use_msi is not None:
            pulumi.set(__self__, "use_msi", use_msi)
        if use_oidc is not None:
            pulumi.set(__self__, "use_oidc", use_oidc)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Input[str]:
        """
        The Cloud Environment which should be used. Possible values are public, usgovernment and china. Defaults to public.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="auxiliaryTenantIds")
    def auxiliary_tenant_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "auxiliary_tenant_ids")

    @auxiliary_tenant_ids.setter
    def auxiliary_tenant_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "auxiliary_tenant_ids", value)

    @property
    @pulumi.getter(name="clientCertificatePassword")
    def client_certificate_password(self) -> Optional[pulumi.Input[str]]:
        """
        The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client
        Certificate
        """
        return pulumi.get(self, "client_certificate_password")

    @client_certificate_password.setter
    def client_certificate_password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate_password", value)

    @property
    @pulumi.getter(name="clientCertificatePath")
    def client_certificate_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
        Principal using a Client Certificate.
        """
        return pulumi.get(self, "client_certificate_path")

    @client_certificate_path.setter
    def client_certificate_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_certificate_path", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Client ID which should be used.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter(name="customCorrelationRequestId")
    def custom_correlation_request_id(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the x-ms-correlation-request-id header (otherwise an auto-generated UUID will be used).
        """
        return pulumi.get(self, "custom_correlation_request_id")

    @custom_correlation_request_id.setter
    def custom_correlation_request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_correlation_request_id", value)

    @property
    @pulumi.getter(name="defaultLocation")
    def default_location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_location")

    @default_location.setter
    def default_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_location", value)

    @property
    @pulumi.getter(name="defaultName")
    def default_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_name")

    @default_name.setter
    def default_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_name", value)

    @property
    @pulumi.getter(name="defaultNamingPrefix")
    def default_naming_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_naming_prefix")

    @default_naming_prefix.setter
    def default_naming_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_naming_prefix", value)

    @property
    @pulumi.getter(name="defaultNamingSuffix")
    def default_naming_suffix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "default_naming_suffix")

    @default_naming_suffix.setter
    def default_naming_suffix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_naming_suffix", value)

    @property
    @pulumi.getter(name="defaultTags")
    def default_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "default_tags")

    @default_tags.setter
    def default_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "default_tags", value)

    @property
    @pulumi.getter(name="disableCorrelationRequestId")
    def disable_correlation_request_id(self) -> Optional[pulumi.Input[bool]]:
        """
        This will disable the x-ms-correlation-request-id header.
        """
        return pulumi.get(self, "disable_correlation_request_id")

    @disable_correlation_request_id.setter
    def disable_correlation_request_id(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_correlation_request_id", value)

    @property
    @pulumi.getter(name="disableTerraformPartnerId")
    def disable_terraform_partner_id(self) -> Optional[pulumi.Input[bool]]:
        """
        This will disable the Terraform Partner ID which is used if a custom `partner_id` isn't specified.
        """
        return pulumi.get(self, "disable_terraform_partner_id")

    @disable_terraform_partner_id.setter
    def disable_terraform_partner_id(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_terraform_partner_id", value)

    @property
    @pulumi.getter(name="oidcRequestToken")
    def oidc_request_token(self) -> Optional[pulumi.Input[str]]:
        """
        The bearer token for the request to the OIDC provider. For use When authenticating as a Service Principal using OpenID
        Connect.
        """
        return pulumi.get(self, "oidc_request_token")

    @oidc_request_token.setter
    def oidc_request_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_request_token", value)

    @property
    @pulumi.getter(name="oidcRequestUrl")
    def oidc_request_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL for the OIDC provider from which to request an ID token. For use When authenticating as a Service Principal
        using OpenID Connect.
        """
        return pulumi.get(self, "oidc_request_url")

    @oidc_request_url.setter
    def oidc_request_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_request_url", value)

    @property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> Optional[pulumi.Input[str]]:
        """
        The OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        """
        return pulumi.get(self, "oidc_token")

    @oidc_token.setter
    def oidc_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_token", value)

    @property
    @pulumi.getter(name="oidcTokenFilePath")
    def oidc_token_file_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path to a file containing an OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        """
        return pulumi.get(self, "oidc_token_file_path")

    @oidc_token_file_path.setter
    def oidc_token_file_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oidc_token_file_path", value)

    @property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> Optional[pulumi.Input[str]]:
        """
        A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
        """
        return pulumi.get(self, "partner_id")

    @partner_id.setter
    def partner_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_id", value)

    @property
    @pulumi.getter(name="skipProviderRegistration")
    def skip_provider_registration(self) -> Optional[pulumi.Input[bool]]:
        """
        Should the Provider skip registering all of the Resource Providers that it supports, if they're not already registered?
        """
        return pulumi.get(self, "skip_provider_registration")

    @skip_provider_registration.setter
    def skip_provider_registration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_provider_registration", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Subscription ID which should be used.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Tenant ID which should be used.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter(name="useCli")
    def use_cli(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow Azure CLI to be used for Authentication.
        """
        return pulumi.get(self, "use_cli")

    @use_cli.setter
    def use_cli(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_cli", value)

    @property
    @pulumi.getter(name="useMsi")
    def use_msi(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow Managed Service Identity to be used for Authentication.
        """
        return pulumi.get(self, "use_msi")

    @use_msi.setter
    def use_msi(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_msi", value)

    @property
    @pulumi.getter(name="useOidc")
    def use_oidc(self) -> Optional[pulumi.Input[bool]]:
        """
        Allow OpenID Connect to be used for authentication
        """
        return pulumi.get(self, "use_oidc")

    @use_oidc.setter
    def use_oidc(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_oidc", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auxiliary_tenant_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_certificate_password: Optional[pulumi.Input[str]] = None,
                 client_certificate_path: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 custom_correlation_request_id: Optional[pulumi.Input[str]] = None,
                 default_location: Optional[pulumi.Input[str]] = None,
                 default_name: Optional[pulumi.Input[str]] = None,
                 default_naming_prefix: Optional[pulumi.Input[str]] = None,
                 default_naming_suffix: Optional[pulumi.Input[str]] = None,
                 default_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 disable_correlation_request_id: Optional[pulumi.Input[bool]] = None,
                 disable_terraform_partner_id: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 oidc_request_token: Optional[pulumi.Input[str]] = None,
                 oidc_request_url: Optional[pulumi.Input[str]] = None,
                 oidc_token: Optional[pulumi.Input[str]] = None,
                 oidc_token_file_path: Optional[pulumi.Input[str]] = None,
                 partner_id: Optional[pulumi.Input[str]] = None,
                 skip_provider_registration: Optional[pulumi.Input[bool]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 use_cli: Optional[pulumi.Input[bool]] = None,
                 use_msi: Optional[pulumi.Input[bool]] = None,
                 use_oidc: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The provider type for the azapi package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] client_certificate_password: The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client
               Certificate
        :param pulumi.Input[str] client_certificate_path: The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
               Principal using a Client Certificate.
        :param pulumi.Input[str] client_id: The Client ID which should be used.
        :param pulumi.Input[str] client_secret: The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.
        :param pulumi.Input[str] custom_correlation_request_id: The value of the x-ms-correlation-request-id header (otherwise an auto-generated UUID will be used).
        :param pulumi.Input[bool] disable_correlation_request_id: This will disable the x-ms-correlation-request-id header.
        :param pulumi.Input[bool] disable_terraform_partner_id: This will disable the Terraform Partner ID which is used if a custom `partner_id` isn't specified.
        :param pulumi.Input[str] environment: The Cloud Environment which should be used. Possible values are public, usgovernment and china. Defaults to public.
        :param pulumi.Input[str] oidc_request_token: The bearer token for the request to the OIDC provider. For use When authenticating as a Service Principal using OpenID
               Connect.
        :param pulumi.Input[str] oidc_request_url: The URL for the OIDC provider from which to request an ID token. For use When authenticating as a Service Principal
               using OpenID Connect.
        :param pulumi.Input[str] oidc_token: The OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        :param pulumi.Input[str] oidc_token_file_path: The path to a file containing an OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        :param pulumi.Input[str] partner_id: A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
        :param pulumi.Input[bool] skip_provider_registration: Should the Provider skip registering all of the Resource Providers that it supports, if they're not already registered?
        :param pulumi.Input[str] subscription_id: The Subscription ID which should be used.
        :param pulumi.Input[str] tenant_id: The Tenant ID which should be used.
        :param pulumi.Input[bool] use_cli: Allow Azure CLI to be used for Authentication.
        :param pulumi.Input[bool] use_msi: Allow Managed Service Identity to be used for Authentication.
        :param pulumi.Input[bool] use_oidc: Allow OpenID Connect to be used for authentication
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the azapi package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auxiliary_tenant_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 client_certificate_password: Optional[pulumi.Input[str]] = None,
                 client_certificate_path: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 custom_correlation_request_id: Optional[pulumi.Input[str]] = None,
                 default_location: Optional[pulumi.Input[str]] = None,
                 default_name: Optional[pulumi.Input[str]] = None,
                 default_naming_prefix: Optional[pulumi.Input[str]] = None,
                 default_naming_suffix: Optional[pulumi.Input[str]] = None,
                 default_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 disable_correlation_request_id: Optional[pulumi.Input[bool]] = None,
                 disable_terraform_partner_id: Optional[pulumi.Input[bool]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 oidc_request_token: Optional[pulumi.Input[str]] = None,
                 oidc_request_url: Optional[pulumi.Input[str]] = None,
                 oidc_token: Optional[pulumi.Input[str]] = None,
                 oidc_token_file_path: Optional[pulumi.Input[str]] = None,
                 partner_id: Optional[pulumi.Input[str]] = None,
                 skip_provider_registration: Optional[pulumi.Input[bool]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 use_cli: Optional[pulumi.Input[bool]] = None,
                 use_msi: Optional[pulumi.Input[bool]] = None,
                 use_oidc: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["auxiliary_tenant_ids"] = pulumi.Output.from_input(auxiliary_tenant_ids).apply(pulumi.runtime.to_json) if auxiliary_tenant_ids is not None else None
            __props__.__dict__["client_certificate_password"] = client_certificate_password
            __props__.__dict__["client_certificate_path"] = client_certificate_path
            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["client_secret"] = client_secret
            __props__.__dict__["custom_correlation_request_id"] = custom_correlation_request_id
            __props__.__dict__["default_location"] = default_location
            __props__.__dict__["default_name"] = default_name
            __props__.__dict__["default_naming_prefix"] = default_naming_prefix
            __props__.__dict__["default_naming_suffix"] = default_naming_suffix
            __props__.__dict__["default_tags"] = pulumi.Output.from_input(default_tags).apply(pulumi.runtime.to_json) if default_tags is not None else None
            __props__.__dict__["disable_correlation_request_id"] = pulumi.Output.from_input(disable_correlation_request_id).apply(pulumi.runtime.to_json) if disable_correlation_request_id is not None else None
            __props__.__dict__["disable_terraform_partner_id"] = pulumi.Output.from_input(disable_terraform_partner_id).apply(pulumi.runtime.to_json) if disable_terraform_partner_id is not None else None
            if environment is None and not opts.urn:
                raise TypeError("Missing required property 'environment'")
            __props__.__dict__["environment"] = environment
            __props__.__dict__["oidc_request_token"] = oidc_request_token
            __props__.__dict__["oidc_request_url"] = oidc_request_url
            __props__.__dict__["oidc_token"] = oidc_token
            __props__.__dict__["oidc_token_file_path"] = oidc_token_file_path
            __props__.__dict__["partner_id"] = partner_id
            __props__.__dict__["skip_provider_registration"] = pulumi.Output.from_input(skip_provider_registration).apply(pulumi.runtime.to_json) if skip_provider_registration is not None else None
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["use_cli"] = pulumi.Output.from_input(use_cli).apply(pulumi.runtime.to_json) if use_cli is not None else None
            __props__.__dict__["use_msi"] = pulumi.Output.from_input(use_msi).apply(pulumi.runtime.to_json) if use_msi is not None else None
            __props__.__dict__["use_oidc"] = pulumi.Output.from_input(use_oidc).apply(pulumi.runtime.to_json) if use_oidc is not None else None
        super(Provider, __self__).__init__(
            'azapi',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="clientCertificatePassword")
    def client_certificate_password(self) -> pulumi.Output[Optional[str]]:
        """
        The password associated with the Client Certificate. For use when authenticating as a Service Principal using a Client
        Certificate
        """
        return pulumi.get(self, "client_certificate_password")

    @property
    @pulumi.getter(name="clientCertificatePath")
    def client_certificate_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path to the Client Certificate associated with the Service Principal for use when authenticating as a Service
        Principal using a Client Certificate.
        """
        return pulumi.get(self, "client_certificate_path")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Client ID which should be used.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[Optional[str]]:
        """
        The Client Secret which should be used. For use When authenticating as a Service Principal using a Client Secret.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="customCorrelationRequestId")
    def custom_correlation_request_id(self) -> pulumi.Output[Optional[str]]:
        """
        The value of the x-ms-correlation-request-id header (otherwise an auto-generated UUID will be used).
        """
        return pulumi.get(self, "custom_correlation_request_id")

    @property
    @pulumi.getter(name="defaultLocation")
    def default_location(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_location")

    @property
    @pulumi.getter(name="defaultName")
    def default_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_name")

    @property
    @pulumi.getter(name="defaultNamingPrefix")
    def default_naming_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_naming_prefix")

    @property
    @pulumi.getter(name="defaultNamingSuffix")
    def default_naming_suffix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "default_naming_suffix")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[str]:
        """
        The Cloud Environment which should be used. Possible values are public, usgovernment and china. Defaults to public.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="oidcRequestToken")
    def oidc_request_token(self) -> pulumi.Output[Optional[str]]:
        """
        The bearer token for the request to the OIDC provider. For use When authenticating as a Service Principal using OpenID
        Connect.
        """
        return pulumi.get(self, "oidc_request_token")

    @property
    @pulumi.getter(name="oidcRequestUrl")
    def oidc_request_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL for the OIDC provider from which to request an ID token. For use When authenticating as a Service Principal
        using OpenID Connect.
        """
        return pulumi.get(self, "oidc_request_url")

    @property
    @pulumi.getter(name="oidcToken")
    def oidc_token(self) -> pulumi.Output[Optional[str]]:
        """
        The OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        """
        return pulumi.get(self, "oidc_token")

    @property
    @pulumi.getter(name="oidcTokenFilePath")
    def oidc_token_file_path(self) -> pulumi.Output[Optional[str]]:
        """
        The path to a file containing an OIDC ID token for use when authenticating as a Service Principal using OpenID Connect.
        """
        return pulumi.get(self, "oidc_token_file_path")

    @property
    @pulumi.getter(name="partnerId")
    def partner_id(self) -> pulumi.Output[Optional[str]]:
        """
        A GUID/UUID that is registered with Microsoft to facilitate partner resource usage attribution.
        """
        return pulumi.get(self, "partner_id")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Subscription ID which should be used.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Tenant ID which should be used.
        """
        return pulumi.get(self, "tenant_id")

