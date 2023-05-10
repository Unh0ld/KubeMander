# AutoGPT-Kubernetes Plugin 🐳

An AutoGPT plugin to enable interaction with Kubernetes for managing applications and resources.

## 📚 Requirements

1. **Kubernetes Configuration**: Ensure that you have a configured `kubeconfig` file for connecting to your Kubernetes cluster. You can obtain this from your Kubernetes cluster administrator or create it yourself if you are the administrator.

2. **kubectl**: The Kubernetes command-line tool, `kubectl`, must be installed and accessible from the system's PATH. You can verify this by running `kubectl version` in your terminal.

## 🔧 Configuration

1. **Update the .env file**: Add the following lines to your `.env` file:

```
################################################################################
### KUBERNETES PLUGIN SETTINGS
################################################################################

KUBECONFIG_PATH = path_to_your_kubeconfig_file
```

2. **Allowlist Plugin**: In your `.env` file, search for `ALLOWLISTED_PLUGINS` and add this plugin:

```
################################################################################
ALLOWLISTED PLUGINS
################################################################################

#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTKubernetes
```


## 🚀 Usage

After configuring the settings, you can use the AutoGPT-Kubernetes plugin to allow AutoGPT to manage applications and resources in Kubernetes.

Example:

1. **Configure Auto-GPT**: Set up Auto-GPT with the following parameters:
- Name: `K8sManagerGPT`
- Role: `an ai designed to manage Kubernetes resources`
- Goals:
  1. Goal 1: `Deploy an application using the nginx image`
  2. Goal 2: `Terminate`

2. **Run Auto-GPT**: Launch Auto-GPT, which should use the Kubernetes plugin to deploy the application and return the status.
