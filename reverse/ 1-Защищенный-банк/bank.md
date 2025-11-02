## task
### Описание
Я забыл свой пин-код, но мне очень нужны деньги, помоги мне пожалуйста

### Исходники
protected_bank.exe

## wtriteup
открываем в ida + f5 (pseudocode)

```pseudocode
int __fastcall main(int argc, const char **argv, const char **envp)
{
  FILE *v3; // rax
  char Buffer[128]; // [rsp+20h] [rbp-80h] BYREF
  _main(argc, argv, envp);
  puts_0("Welcome to the 'NotScam'");
  printf("To withdraw money, enter your pin: ");
  v3 = __acrt_iob_func(0);
  fgets_0(Buffer, 128, v3);
  if ( Buffer[12] == 18 && Buffer[120] )
  {
    puts_0("Yes!!!");
    puts_0("DUCKERZ{StR1ing3_s0lv3_th1s_B1NK}");
  }
  else
  {
    puts_0("Incorrect password");
  }
  return 0;
}
```

## flag
```flag
DUCKERZ{StR1ing3_s0lv3_th1s_B1NK}
```