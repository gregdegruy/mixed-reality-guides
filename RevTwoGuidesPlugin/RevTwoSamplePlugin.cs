using Microsoft.Xrm.Sdk;
using System;
using System.ServiceModel;

namespace RevTwoGuidesPlugin
{
    /* 
     * Plugin development guide: https://docs.microsoft.com/powerapps/developer/common-data-service/plug-ins
     * Best practices and guidance: https://docs.microsoft.com/powerapps/developer/common-data-service/best-practices/business-logic/
     */
    public class RevTwoSamplePlugin : PluginBase
    {
        public RevTwoSamplePlugin(string unsecureConfiguration, string secureConfiguration)
            : base(typeof(RevTwoSamplePlugin))
        {
            // TODO: Implement your custom configuration handling
            // https://docs.microsoft.com/powerapps/developer/common-data-service/register-plug-in#set-configuration-data
        }

        // Entry point for custom business logic execution
        protected override void ExecuteCdsPlugin(ILocalPluginContext localPluginContext)
        {
            if (localPluginContext == null)
            {
                throw new ArgumentNullException("localPluginContext");
            }

            IPluginExecutionContext context = localPluginContext.PluginExecutionContext;
             
            // Check for the entity on which the plugin would be registered
            if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity)
            {
                Entity entity = (Entity)context.InputParameters["Target"];

                if (entity.LogicalName == "account")
                {
                    try
                    {
                        Entity followup = new Entity("task");

                        followup["subject"] = "Send e-mail to the new customer.";
                        followup["description"] =
                            "Follow up with the customer. Check if there are any new issues that need resolution.";
                        followup["scheduledstart"] = DateTime.Now.AddDays(7);
                        followup["scheduledend"] = DateTime.Now.AddDays(7);
                        followup["category"] = context.PrimaryEntityName;

                        if (context.OutputParameters.Contains("id"))
                        {
                            Guid regardingobjectid = new Guid(context.OutputParameters["id"].ToString());
                            string regardingobjectidType = "account";

                            followup["regardingobjectid"] =
                            new EntityReference(regardingobjectidType, regardingobjectid);
                        }

                        localPluginContext.Trace("FollowupPlugin: Creating the task activity.");
                        localPluginContext.CurrentUserService.Create(followup);
                    }

                    catch (FaultException<OrganizationServiceFault> ex)
                    {
                        throw new InvalidPluginExecutionException("An error occurred in FollowUpPlugin.", ex);
                    }

                    catch (Exception ex)
                    {
                        localPluginContext.Trace("FollowUpPlugin: " + ex.ToString());
                        throw;
                    }
                }
            }
        }
    }
}