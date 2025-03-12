import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    {
        "col1": list(range(20)),
        "col2": np.random.randn(20),
        "col3": np.random.randn(20),
    }
)

st.bar_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF00FF", "#4B0082"],  # Optional
)


# import streamlit as st
# import pandas as pd
# import numpy as np

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.bar_chart(chart_data)

# import streamlit as st
# import pandas as pd
# import numpy as np

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3), columns=["col1", "col2", "col3"]
# )

# st.line_chart(
#     chart_data,
#     x="col1",
#     y=["col2", "col3"],
#     color=["#800000", "#808000"],  # Optional
# )



# import streamlit as st
# import pandas as pd
# import numpy as np

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
# print(chart_data)
# st.line_chart(chart_data)

