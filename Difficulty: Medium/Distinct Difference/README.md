<h2><a href="https://www.geeksforgeeks.org/problems/distinct-difference--170647/1">Distinct Difference</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Given an array <strong>arr[]</strong> of size <strong>n</strong>, for each index i, find the difference between the number of distinct elements to the left of arr[i] and the number of distinct elements to the right of arr[i].</span></p>
<p><span style="font-size: 18px;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>: arr[] = [4, 3, 3]
<strong>Output:</strong> [-1, 0, 2]
<strong>Explanation</strong>: For index i = 1, there are 0 distinct elements on the left side and 1 distinct on its right. So difference is 0 - 1 = -1. </span>
<span style="font-size: 18px;">For index i = 2, there is 1 distinct element on the left, and 1 distinct element on its right. So difference is 1-1 = 0.</span>
<span style="font-size: 18px;">For index i = 3, there are 2 distinct (4 and 3) on left, and 0 distinct on its left. So difference is 2-0 = 2.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [4, 4, 3, 3]
<strong>Output: </strong>[-2, 0, 0, 2]
<strong>Explanation</strong>: For index i = 1, difference is 0 - 2 = -2.
</span><span style="font-size: 18px;">For index i = 2, difference is 1 - 1 = 0.</span>
<span style="font-size: 18px;">For index i = 4, difference is 2 - 0 = 2.</span></pre></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Set</code>&nbsp;<code>Arrays</code>&nbsp;<code>Map</code>&nbsp;