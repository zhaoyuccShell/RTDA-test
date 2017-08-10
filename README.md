## Dash On-Premise Sample App

This repository contains a simple Dash app that can be deployed as-is on your [Plotly On-Premise](https://plot.ly/products/on-premise) server.

#### Deployment Instructions

To learn more about what each of these files does and how to start from scratch, see the [Plotly On-Premise Dash App Deployment Docs](https://plot.ly/dash/deployment/on-premise).

1. Git clone this repo
```
git clone https://github.com/plotly/dash-on-premise-sample-app.git
```

2. Create an SSH Key

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

3. Upload that SSH Key to your Dash App Manager
![Dash App Manager SSH Key](https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-ssh-key.png)

4. Create an app on the Dash App Manager
Visit the Dash App Manager, log in, and click "Add an app".
![Dash App Manager](https://github.com/plotly/dash-docs/raw/master/images/dash-app-manager-launch-app.png)

5. Add Plotly On-Premise as a Git Remote
```
git remote add plotly dokku@your-dash-app-manager-domain:your-dash-app-name
```

Replace `your-dash-app-manager` with the domain of your Dash app domain (without `https://` or `http://`) and `your-dash-app-name` with the name of the Dash app that you created in Step 4.

6. Push the code to Plotly On-Premise
```
git push plotly master
```

7. View your app

