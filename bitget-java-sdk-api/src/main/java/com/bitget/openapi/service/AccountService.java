package com.bitget.openapi.service;


import com.bitget.openapi.dto.request.AdjustMarginReq;
import com.bitget.openapi.dto.request.AutoAppendMarginReq;
import com.bitget.openapi.dto.request.ChangeLeverageReq;
import com.bitget.openapi.dto.request.LedgerReq;
import com.bitget.openapi.dto.response.*;

import java.io.IOException;
import java.util.List;

/**
 * 持仓服务
 * @author bitget-sdk-team
 * @date 2019-01-15
 */
public interface AccountService {
    /**
     * 查询所有合约账户信息
     * @return
     * @throws IOException
     */
     List<AccountInfo> accounts() throws IOException;

    /**
     * 单个合约账户信息
     * @param symbol
     * @return
     * @throws IOException
     */
    AccountInfo getAccount(String symbol) throws IOException;

    /**
     * 获取单个合约的用户配置
     * @param symbol
     * @return
     * @throws IOException
     */
    AccountSetting settings(String symbol) throws IOException;

    /**
     * 调整杠杆
     * @param symbol
     * @param changeLeverageReq
     * @return
     * @throws IOException
     */
    ChangeLeverageResult leverage(String symbol, ChangeLeverageReq changeLeverageReq) throws IOException;

    /**
     * 列出主账户资产流水
     * @param symbol
     * @param ledgerReq
     * @return
     * @throws IOException
     */
    List<LedgerResult> getLedger(String symbol, LedgerReq ledgerReq) throws IOException;

    /**
     * 列出保证金账户资产流水
     * @param symbol
     * @param ledgerReq
     * @return
     * @throws IOException
     */
    List<LedgerResult> ledgerMargin(String symbol, LedgerReq ledgerReq) throws IOException;

    /**
     * 调整保证金
     * @param symbol
     * @param adjustMarginReq
     * @return
     * @throws IOException
     */
    AdjustMarginResult adjustMargin(String symbol, AdjustMarginReq adjustMarginReq) throws IOException;
    /**
     * 列出保证金账户资产流水
     * @param symbol
     * @param autoAppendMarginReq
     * @return
     * @throws IOException
     */
    AutoAppendMarginResult modifyAutoAppendMargin(String symbol, AutoAppendMarginReq autoAppendMarginReq) throws IOException;
}
