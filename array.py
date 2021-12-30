family = [
          ['SJ family', 'vyas', 'appa', 'amma', 'shivani', 'gopal thatha', 'nataraj thatha', 'lakshmi patti', 'santha patti'],
          ['Boston family', 'aravind', 'taran', 'suji perimma', 'uday perippa' ],
          ['German family', 'athreya', 'prem chithi', 'narayan chithappa'],
          ['colorado family', 'nikita', 'isha', 'piefacemommyaunty', 'kumarperippa']
          ];

for group in family:
    i = 0;
    for member in group:
        if i == 0:
            i = i+1;
            continue;

        print(group[0], 'member', i, 'is', member);
        i = i + 1
