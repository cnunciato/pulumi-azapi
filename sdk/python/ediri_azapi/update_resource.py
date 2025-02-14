# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UpdateResourceArgs', 'UpdateResource']

@pulumi.input_type
class UpdateResourceArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 body: Optional[pulumi.Input[str]] = None,
                 ignore_casing: Optional[pulumi.Input[bool]] = None,
                 ignore_missing_property: Optional[pulumi.Input[bool]] = None,
                 locks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 response_export_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a UpdateResource resource.
        :param pulumi.Input[str] type: It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
               `<api-version>` is version of the API used to manage this azure resource.
        :param pulumi.Input[str] body: A JSON object that contains the request body used to add on an existing azure resource.
        :param pulumi.Input[bool] ignore_casing: Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        :param pulumi.Input[bool] ignore_missing_property: Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locks: A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        :param pulumi.Input[str] name: Specifies the name of the azure resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] parent_id: The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
               - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
               - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
               - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
               - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
               - tenant scope: `parent_id` should be `/`
               
               For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        :param pulumi.Input[str] resource_id: The ID of an existing azure source. Changing this forces a new azure resource to be created.
               
               > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] response_export_values: A list of path that needs to be exported from response body.
               Setting it to `["*"]` will export the full response body.
               Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
               ```
               {
               "properties" : {
               "loginServer" : "registry1.azurecr.io"
               "policies" : {
               "quarantinePolicy" = {
               "status" = "disabled"
               }
               }
               }
               }
               ```
        """
        pulumi.set(__self__, "type", type)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if ignore_casing is not None:
            pulumi.set(__self__, "ignore_casing", ignore_casing)
        if ignore_missing_property is not None:
            pulumi.set(__self__, "ignore_missing_property", ignore_missing_property)
        if locks is not None:
            pulumi.set(__self__, "locks", locks)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if response_export_values is not None:
            pulumi.set(__self__, "response_export_values", response_export_values)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
        `<api-version>` is version of the API used to manage this azure resource.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        A JSON object that contains the request body used to add on an existing azure resource.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="ignoreCasing")
    def ignore_casing(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_casing")

    @ignore_casing.setter
    def ignore_casing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_casing", value)

    @property
    @pulumi.getter(name="ignoreMissingProperty")
    def ignore_missing_property(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        """
        return pulumi.get(self, "ignore_missing_property")

    @ignore_missing_property.setter
    def ignore_missing_property(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_missing_property", value)

    @property
    @pulumi.getter
    def locks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        """
        return pulumi.get(self, "locks")

    @locks.setter
    def locks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locks", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the azure resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
        - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
        - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
        - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
        - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
        - tenant scope: `parent_id` should be `/`

        For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an existing azure source. Changing this forces a new azure resource to be created.

        > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="responseExportValues")
    def response_export_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of path that needs to be exported from response body.
        Setting it to `["*"]` will export the full response body.
        Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
        ```
        {
        "properties" : {
        "loginServer" : "registry1.azurecr.io"
        "policies" : {
        "quarantinePolicy" = {
        "status" = "disabled"
        }
        }
        }
        }
        ```
        """
        return pulumi.get(self, "response_export_values")

    @response_export_values.setter
    def response_export_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "response_export_values", value)


@pulumi.input_type
class _UpdateResourceState:
    def __init__(__self__, *,
                 body: Optional[pulumi.Input[str]] = None,
                 ignore_casing: Optional[pulumi.Input[bool]] = None,
                 ignore_missing_property: Optional[pulumi.Input[bool]] = None,
                 locks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 response_export_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UpdateResource resources.
        :param pulumi.Input[str] body: A JSON object that contains the request body used to add on an existing azure resource.
        :param pulumi.Input[bool] ignore_casing: Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        :param pulumi.Input[bool] ignore_missing_property: Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locks: A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        :param pulumi.Input[str] name: Specifies the name of the azure resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] output: The output json containing the properties specified in `response_export_values`. Here're some examples to decode json and extract the value.
               ```
               // it will output "registry1.azurecr.io"
               output "login_server" {
               value = jsondecode(azapi_resource.example.output).properties.loginServer
               }
        :param pulumi.Input[str] parent_id: The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
               - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
               - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
               - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
               - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
               - tenant scope: `parent_id` should be `/`
               
               For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        :param pulumi.Input[str] resource_id: The ID of an existing azure source. Changing this forces a new azure resource to be created.
               
               > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] response_export_values: A list of path that needs to be exported from response body.
               Setting it to `["*"]` will export the full response body.
               Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
               ```
               {
               "properties" : {
               "loginServer" : "registry1.azurecr.io"
               "policies" : {
               "quarantinePolicy" = {
               "status" = "disabled"
               }
               }
               }
               }
               ```
        :param pulumi.Input[str] type: It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
               `<api-version>` is version of the API used to manage this azure resource.
        """
        if body is not None:
            pulumi.set(__self__, "body", body)
        if ignore_casing is not None:
            pulumi.set(__self__, "ignore_casing", ignore_casing)
        if ignore_missing_property is not None:
            pulumi.set(__self__, "ignore_missing_property", ignore_missing_property)
        if locks is not None:
            pulumi.set(__self__, "locks", locks)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if output is not None:
            pulumi.set(__self__, "output", output)
        if parent_id is not None:
            pulumi.set(__self__, "parent_id", parent_id)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if response_export_values is not None:
            pulumi.set(__self__, "response_export_values", response_export_values)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        A JSON object that contains the request body used to add on an existing azure resource.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="ignoreCasing")
    def ignore_casing(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_casing")

    @ignore_casing.setter
    def ignore_casing(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_casing", value)

    @property
    @pulumi.getter(name="ignoreMissingProperty")
    def ignore_missing_property(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        """
        return pulumi.get(self, "ignore_missing_property")

    @ignore_missing_property.setter
    def ignore_missing_property(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_missing_property", value)

    @property
    @pulumi.getter
    def locks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        """
        return pulumi.get(self, "locks")

    @locks.setter
    def locks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locks", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the azure resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input[str]]:
        """
        The output json containing the properties specified in `response_export_values`. Here're some examples to decode json and extract the value.
        ```
        // it will output "registry1.azurecr.io"
        output "login_server" {
        value = jsondecode(azapi_resource.example.output).properties.loginServer
        }
        """
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output", value)

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
        - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
        - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
        - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
        - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
        - tenant scope: `parent_id` should be `/`

        For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        """
        return pulumi.get(self, "parent_id")

    @parent_id.setter
    def parent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an existing azure source. Changing this forces a new azure resource to be created.

        > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="responseExportValues")
    def response_export_values(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of path that needs to be exported from response body.
        Setting it to `["*"]` will export the full response body.
        Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
        ```
        {
        "properties" : {
        "loginServer" : "registry1.azurecr.io"
        "policies" : {
        "quarantinePolicy" = {
        "status" = "disabled"
        }
        }
        }
        }
        ```
        """
        return pulumi.get(self, "response_export_values")

    @response_export_values.setter
    def response_export_values(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "response_export_values", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
        `<api-version>` is version of the API used to manage this azure resource.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class UpdateResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 ignore_casing: Optional[pulumi.Input[bool]] = None,
                 ignore_missing_property: Optional[pulumi.Input[bool]] = None,
                 locks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 response_export_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource can manage a subset of any existing Azure resource manager resource's properties.

        > **Note** This resource is used to add or modify properties on an existing resource.
        When delete `UpdateResource`, no operation will be performed, and these properties will stay unchanged.
        If you want to restore the modified properties to some values, you must apply the restored properties before deleting.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: A JSON object that contains the request body used to add on an existing azure resource.
        :param pulumi.Input[bool] ignore_casing: Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        :param pulumi.Input[bool] ignore_missing_property: Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locks: A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        :param pulumi.Input[str] name: Specifies the name of the azure resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] parent_id: The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
               - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
               - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
               - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
               - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
               - tenant scope: `parent_id` should be `/`
               
               For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        :param pulumi.Input[str] resource_id: The ID of an existing azure source. Changing this forces a new azure resource to be created.
               
               > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] response_export_values: A list of path that needs to be exported from response body.
               Setting it to `["*"]` will export the full response body.
               Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
               ```
               {
               "properties" : {
               "loginServer" : "registry1.azurecr.io"
               "policies" : {
               "quarantinePolicy" = {
               "status" = "disabled"
               }
               }
               }
               }
               ```
        :param pulumi.Input[str] type: It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
               `<api-version>` is version of the API used to manage this azure resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UpdateResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource can manage a subset of any existing Azure resource manager resource's properties.

        > **Note** This resource is used to add or modify properties on an existing resource.
        When delete `UpdateResource`, no operation will be performed, and these properties will stay unchanged.
        If you want to restore the modified properties to some values, you must apply the restored properties before deleting.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param UpdateResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UpdateResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 ignore_casing: Optional[pulumi.Input[bool]] = None,
                 ignore_missing_property: Optional[pulumi.Input[bool]] = None,
                 locks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parent_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 response_export_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UpdateResourceArgs.__new__(UpdateResourceArgs)

            __props__.__dict__["body"] = body
            __props__.__dict__["ignore_casing"] = ignore_casing
            __props__.__dict__["ignore_missing_property"] = ignore_missing_property
            __props__.__dict__["locks"] = locks
            __props__.__dict__["name"] = name
            __props__.__dict__["parent_id"] = parent_id
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["response_export_values"] = response_export_values
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["output"] = None
        super(UpdateResource, __self__).__init__(
            'azapi:index/updateResource:UpdateResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            body: Optional[pulumi.Input[str]] = None,
            ignore_casing: Optional[pulumi.Input[bool]] = None,
            ignore_missing_property: Optional[pulumi.Input[bool]] = None,
            locks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            output: Optional[pulumi.Input[str]] = None,
            parent_id: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None,
            response_export_values: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'UpdateResource':
        """
        Get an existing UpdateResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: A JSON object that contains the request body used to add on an existing azure resource.
        :param pulumi.Input[bool] ignore_casing: Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        :param pulumi.Input[bool] ignore_missing_property: Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locks: A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        :param pulumi.Input[str] name: Specifies the name of the azure resource. Changing this forces a new resource to be created.
        :param pulumi.Input[str] output: The output json containing the properties specified in `response_export_values`. Here're some examples to decode json and extract the value.
               ```
               // it will output "registry1.azurecr.io"
               output "login_server" {
               value = jsondecode(azapi_resource.example.output).properties.loginServer
               }
        :param pulumi.Input[str] parent_id: The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
               - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
               - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
               - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
               - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
               - tenant scope: `parent_id` should be `/`
               
               For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        :param pulumi.Input[str] resource_id: The ID of an existing azure source. Changing this forces a new azure resource to be created.
               
               > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] response_export_values: A list of path that needs to be exported from response body.
               Setting it to `["*"]` will export the full response body.
               Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
               ```
               {
               "properties" : {
               "loginServer" : "registry1.azurecr.io"
               "policies" : {
               "quarantinePolicy" = {
               "status" = "disabled"
               }
               }
               }
               }
               ```
        :param pulumi.Input[str] type: It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
               `<api-version>` is version of the API used to manage this azure resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UpdateResourceState.__new__(_UpdateResourceState)

        __props__.__dict__["body"] = body
        __props__.__dict__["ignore_casing"] = ignore_casing
        __props__.__dict__["ignore_missing_property"] = ignore_missing_property
        __props__.__dict__["locks"] = locks
        __props__.__dict__["name"] = name
        __props__.__dict__["output"] = output
        __props__.__dict__["parent_id"] = parent_id
        __props__.__dict__["resource_id"] = resource_id
        __props__.__dict__["response_export_values"] = response_export_values
        __props__.__dict__["type"] = type
        return UpdateResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[Optional[str]]:
        """
        A JSON object that contains the request body used to add on an existing azure resource.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="ignoreCasing")
    def ignore_casing(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether ignore incorrect casing returned in `body` to suppress plan-diff. Defaults to `false`.
        """
        return pulumi.get(self, "ignore_casing")

    @property
    @pulumi.getter(name="ignoreMissingProperty")
    def ignore_missing_property(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether ignore not returned properties like credentials in `body` to suppress plan-diff. Defaults to `true`.
        """
        return pulumi.get(self, "ignore_missing_property")

    @property
    @pulumi.getter
    def locks(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of ARM resource IDs which are used to avoid create/modify/delete azapi resources at the same time.
        """
        return pulumi.get(self, "locks")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the azure resource. Changing this forces a new resource to be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def output(self) -> pulumi.Output[str]:
        """
        The output json containing the properties specified in `response_export_values`. Here're some examples to decode json and extract the value.
        ```
        // it will output "registry1.azurecr.io"
        output "login_server" {
        value = jsondecode(azapi_resource.example.output).properties.loginServer
        }
        """
        return pulumi.get(self, "output")

    @property
    @pulumi.getter(name="parentId")
    def parent_id(self) -> pulumi.Output[str]:
        """
        The ID of the azure resource in which this resource is created. Changing this forces a new resource to be created. It supports different kinds of deployment scope for **top level** resources: 
        - resource group scope: `parent_id` should be the ID of a resource group, it's recommended to manage a resource group by azurerm_resource_group.
        - management group scope: `parent_id` should be the ID of a management group, it's recommended to manage a management group by azurerm_management_group.
        - extension scope: `parent_id` should be the ID of the resource you're adding the extension to.
        - subscription scope: `parent_id` should be like `/subscriptions/00000000-0000-0000-0000-000000000000`
        - tenant scope: `parent_id` should be `/`

        For child level resources, the `parent_id` should be the ID of its parent resource, for example, subnet resource's `parent_id` is the ID of the vnet.
        """
        return pulumi.get(self, "parent_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of an existing azure source. Changing this forces a new azure resource to be created.

        > **Note:** Configuring `name` and `parent_id` is an alternative way to configure `resource_id`.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="responseExportValues")
    def response_export_values(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of path that needs to be exported from response body.
        Setting it to `["*"]` will export the full response body.
        Here's an example. If it sets to `["properties.loginServer", "properties.policies.quarantinePolicy.status"]`, it will set the following json to computed property `output`.
        ```
        {
        "properties" : {
        "loginServer" : "registry1.azurecr.io"
        "policies" : {
        "quarantinePolicy" = {
        "status" = "disabled"
        }
        }
        }
        }
        ```
        """
        return pulumi.get(self, "response_export_values")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        It is in a format like `<resource-type>@<api-version>`. `<resource-type>` is the Azure resource type, for example, `Microsoft.Storage/storageAccounts`.
        `<api-version>` is version of the API used to manage this azure resource.
        """
        return pulumi.get(self, "type")

