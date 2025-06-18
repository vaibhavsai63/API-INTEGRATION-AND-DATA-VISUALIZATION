# API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY: CODETECH IT SOLUTIONS
NAME : VAIBHAVA SAI GANGA
INTERN ID:CT06DM777
DOMAIN :PYTHON
DURATION: 4 WEEKS
MENTOR: NEELA SANTOSH


# DESCRIPTION

The two visualizations presented offer a comprehensive insight into weather patterns by comparing real-time weather data of New Delhi, India with a 5-day weather forecast for London, UK. These visual representations serve as crucial tools in understanding both immediate and projected meteorological conditions, aiding in analysis, planning, and decision-making.

The first image is a bar chart titled “Current Weather in New Delhi, IN.” This chart visualizes five key weather parameters: Temperature, Feels Like, Humidity, Pressure, and Wind Speed. Each of these parameters is plotted on the x-axis, while the y-axis represents their corresponding values. The chart shows that atmospheric pressure is significantly higher than all other parameters, around 1000 hPa, which is typical for sea-level conditions. Temperature and feels-like temperature values are similar, suggesting minimal wind chill or heat index effects. Humidity is moderate, and wind speed is relatively low, reflecting calm weather conditions. This visualization effectively uses height differences in bars to convey magnitude, helping users quickly grasp which weather attributes dominate. This plot was generated using Python’s matplotlib and seaborn libraries, as referenced in the script task1.py.

The second image is a line graph showing the “5-Day Weather Forecast for London.” Two different parameters—temperature and humidity—are plotted over time, with temperature shown in red and humidity in blue. The x-axis represents the date and time range from May 19 to May 24, 2025, while the y-axis captures the respective values of temperature (in °C) and humidity (in %). The temperature line fluctuates gently, with peaks and troughs corresponding to diurnal variations, indicating a relatively mild climate. In contrast, humidity values show more variation, sometimes peaking around 90%, which may suggest intermittent rain or overcast conditions typical in London. The time-series format allows users to anticipate future weather trends, a valuable feature for travelers or event planners. This graph emphasizes the importance of continuous monitoring and forecasting rather than relying solely on static data points.

Together, these charts reflect the power of data visualization in weather analytics. The New Delhi plot is suited for a quick, real-time snapshot of local weather, while the London plot provides temporal weather evolution. These visualizations were developed using data fetched from the OpenWeatherMap API, which is integrated into the project via Python code. The development process—documented in the provided explaintion.docx file—includes installing required libraries (requests, pandas, matplotlib, seaborn, and streamlit), fetching data using the API, and rendering the charts either locally or via a web dashboard using Streamlit.

In essence, this project showcases how combining open-source APIs with Python libraries allows for the creation of dynamic, real-world applications. Users can easily change city names, interact with real-time data, and visualize important climate trends. It is a prime example of using data science to enhance practical awareness, making weather insights more accessible and actionable.
