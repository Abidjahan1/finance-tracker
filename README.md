
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Finance Tracker Project</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; }
        h1 { color: #333; }
        h2 { color: #666; }
        ul { list-style-type: disc; margin-left: 20px; }
        pre { background-color: #f4f4f4; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>Finance Tracker Project</h1>
    <h2>Objective</h2>
    <p>The Finance Tracker Project is a Python-based application designed to help users manage their personal finances effectively. It allows users to log their income and expenses, view summaries of their transactions over a specific period, and visualize their financial data with plots.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Add New Transactions:</strong> Log your income and expenses with details like date, amount, category, and a brief description.</li>
        <li><strong>View Transactions and Summary:</strong> Retrieve a detailed list of transactions within a specified date range, including total income, expenses, and net savings.</li>
        <li><strong>Visualize Financial Data:</strong> Generate plots to visualize your income and expenses over time, helping you analyze your spending habits and savings.</li>
    </ul>

    <h2>Usage</h2>
    <ol>
        <li><strong>Initialize and Run:</strong> Run the <code>main.py</code> file to create a CSV file (<code>finance.csv</code>) if it does not already exist.</li>
        <li><strong>Adding a Transaction:</strong> Select the option to add a transaction and provide the required details.</li>
        <li><strong>Viewing Transactions:</strong> Choose the option to view transactions within a date range to get a summary of your financial activity.</li>
        <li><strong>Visualizing Data:</strong> After viewing transactions, you can choose to see a plot of your income and expenses.</li>
    </ol>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>pandas</li>
        <li>matplotlib</li>
    </ul>

    <h2>How to Run</h2>
    <ol>
        <li>Install the required libraries:
            <pre><code>pip install pandas matplotlib</code></pre>
        </li>
        <li>Run the main script:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

    <h2>File Structure</h2>
    <ul>
        <li><code>main.py</code>: Main script to interact with the finance tracker.</li>
        <li><code>data_insert.py</code>: Contains helper functions for data input.</li>
        <li><code>finance.csv</code>: CSV file to store transaction data.</li>
    </ul>
</body>
</html>
