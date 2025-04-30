<!-- Motivational Quote -->
<div align="center" style="font-family:Arial, sans-serif; border:2px dashed #ccc; border-radius:10px; padding:20px; background:#f9f9f9; color:#333; max-width:600px; margin:auto;">
  <h2>For the times when nothing works...</h2>
  <p style="font-size:1.5em; font-style:italic; margin:20px 0;">
    Just put this on your screen for a while and keep contemplating:
  </p>
  <p style="font-size:2em; font-weight:bold; color:#555;">"Gayi bhes paani mein 😊"</p>
</div>

<hr>

<!-- Section: Buffalo Animation -->
<h2>🐃 Create the Buffalo Descending Animation</h2>

<h3>📦 Installation</h3>
<ol>
  <li><strong>Clone this Repository</strong></li>
  <pre><code>git clone https://github.com/arryaanjain/GAYI_BHES_PAANI_MEIN.git
cd GAYI_BHES_PAANI_MEIN
</code></pre>

  <li><strong>Create a Virtual Environment</strong></li>
  <pre><code># Windows
python -m venv venv

# Linux / macOS
python3 -m venv venv
</code></pre>

  <li><strong>Activate the Environment</strong></li>
  <pre><code># Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate
</code></pre>

  <li><strong>Install Dependencies</strong></li>
  <pre><code>pip install pillow</code></pre>
</ol>

<!-- Section: Execution Policy Fix -->
<h3>⚠️ Windows PowerShell Execution Policy Fix</h3>

<p>If you get this error:</p>
<pre><code>activate.ps1 cannot be loaded because running scripts is disabled on this system.</code></pre>

<p><strong>Run this before activating:</strong></p>
<pre><code>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process</code></pre>

<p>Then try:</p>
<pre><code>venv\Scripts\Activate.ps1</code></pre>

<p><em>✅ This only changes the policy for the current terminal session.</em></p>

<p><strong>Optional (Permanent Change, be cautious):</strong></p>
<pre><code>Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser</code></pre>

<hr>

<h3>🚀 Usage</h3>
<p>The Python script inside the repo uses Pillow to animate gayi bhes paani mein 💧.</p>

<p>After setup, run the script with:</p>
<pre><code>python gayi-bhes-paani-mein.py</code></pre>

<p>🎉 Your animated <code>buffalo_descending.gif</code> will be saved in the project directory! Enjoy!</p>
