int generateNum(string S,int i,int j)
{
    int ans=0;
    for(int idx=i;idx<j;idx++)
    {
        ans = ans*10 + S[idx]-'0';
    }
    return ans;
}

bool isValid(string S)
{
    int n=S.length();   
    int i=0;
    while(i<n)
    {
        
        int j=i;
        while(j<n && S[j]!='.')
        {
            j++;
        }
        
        if(j-i>3 || j-i==0)
        {
            return false;
        }
        int num = generateNum(S,i,j);
        
        if(num > 255)
        {
            return false;
        }
        if(j-i>1 && (num==0 || S[i]=='0'))
        {
            return false;
        }
        
        i=j+1;
    }
    
    return true; 
}

string generateString(string A,int i,int j,int k)
{
    string S;
    for(int idx=0;idx<A.length();idx++)
    {
        S=S+A[idx];
    
        if(idx==i || idx==j || idx==k)
        {
            S=S+'.';   
        }
    }
    return S;
}

vector<string> Solution::restoreIpAddresses(string A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int n=A.length();
    vector<string> ans;
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n-1;j++)
        {
            for(int k=j+1;k<n-1;k++)
            {
                string S = generateString(A,i,j,k);
                
                if(isValid(S))
                {
                    ans.push_back(S);
                }
            }
        }
    }
    
    return ans;
}