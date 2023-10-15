python -m pytest tests \
  -v \
  -m "search" \
  --html=./report/html/$(date +%Y-%m-%d-%H-%M-%S)/report.html \
  -n auto
